from src.calculator import calculator as calc
import socket as sock
from src.json import json_handler as json
from src.sockethandler import socket_handler as sh



def handle_connection(conn, addr):
    message = sh.receive_data(conn)
    print('Received: ', message)
    if message != 'shutdown':
        func_list = json.get_list_from_json(message)
        answer = calc.calculate_list(func_list)
        answer_json = json.get_json_from_list(answer)
        print('Sending: ', answer_json)
        sh.send_data(conn, answer_json.encode())
    else:
        return 'shutdown'



def start(host, port):
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
