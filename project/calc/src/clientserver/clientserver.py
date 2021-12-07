from src.json import json_handler as json
from src.sockethandler import socket_handler as sh
import socket as sock
import concurrent.futures


HOST = ''
PORT = 0

SERVER1_HOST = ''
SERVER2_HOST = ''

SERVER1_PORT = 0
SERVER2_PORT = 0

message_list = []


def threaded_socket(args):
    message = json.get_json_from_list(args[2]).encode()
    print(args)
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.connect((args[0], args[1]))
        sh.send_data(s, message)
        s.shutdown(sock.SHUT_WR)
        message = sh.receive_data(s)
        func_list = json.get_list_from_json(message)
        message_list.append(func_list)



def shutdown_server(args):
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.connect((args[0], args[1]))
        sh.send_data(s, args[2])
        s.shutdown(s.SHUT_RDWR)
        s.close()



def handle_connection(conn, addr):
    message = sh.receive_data(conn)
    print('Received: ', message)
    if message != 'shutdown':
        func_list = json.get_list_from_json(message)
        print(func_list)
        i = len(func_list)//2
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(threaded_socket, [(SERVER1_HOST, SERVER1_PORT, func_list[0:i]), (SERVER2_HOST, SERVER2_PORT, func_list[i:len(func_list)])])
        # print(message_list)
        answer = message_list[0] + message_list[1]
        answer_json = json.get_json_from_list(answer)
        print('Sending: ', answer_json)
        sh.send_data(conn, answer_json.encode())
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(shutdown_server, [(SERVER1_HOST, SERVER1_PORT, 'shutdown'), (SERVER2_HOST, SERVER2_PORT, 'shutdown')])
        return 'shutdown'



def start(host, port, server1_host, server1_port, server2_host, server2_port):
    global HOST
    global PORT
    global SERVER1_HOST
    global SERVER1_PORT
    global SERVER2_HOST
    global SERVER2_PORT

    HOST = host
    PORT = port

    SERVER1_HOST = server1_host
    SERVER1_PORT = server1_port

    SERVER2_HOST = server2_host
    SERVER2_PORT = server2_port

    # print(HOST, PORT, SERVER1_HOST, SERVER1_PORT, SERVER2_HOST, SERVER2_PORT)


    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            command = handle_connection(conn, addr)
            conn.close()
            if command == 'shutdown':
                print("shutting down server")
                break
