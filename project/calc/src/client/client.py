from src.json import json_handler as json
import socket as sock
from os import getcwd as getcwd
from src.sockethandler import socket_handler as sh





def read_file(file_path):
    file_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            file_list.append(line.strip())
    return file_list


def shutdown_server(socket):
    sh.send_data(socket, 'shutdown'.encode())


def start(host, port):
    print("Client is running.")
    file_path = 'test/src/functions.txt'
    file_list = read_file(file_path)
    # print(file_list)

    file_json = json.get_json_from_list(file_list)
    # print(file_json)

    message = ''
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        print (host, port)
        s.connect((host, port))
        sh.send_data(s, file_json.encode())
        s.shutdown(sock.SHUT_WR)
        message = sh.receive_data(s)
    print('message received: ', message)


    # with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
    #     s.connect((host, port))
    #     shutdown_server(s)