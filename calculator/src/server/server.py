from src.calculator import calculator as calc
from src.sockethandler import socket_handler as sh
import socket as sock
from src.jsonhandler import json_handler as json


from src.calculator import calculator as calc
import socket as sock
from src.jsonhandler import json_handler as json
from src.sockethandler import socket_handler as sh


def handle_connection(conn, addr):
    # Receive data
    message = sh.receive_data(conn)
    print('Received: ', message)
    if message != 'shutdown':
        # Convert received data from json string to list
        func_list = json.get_list_from_json(message)
        # Calculate the answers from the list
        answer = calc.calculate_list(func_list)
        # Convert the answer list to a json string
        answer_json = json.get_json_from_list(answer)
        print('Sending: ', answer_json)
        # Send the data over the socket as a UTF-8 encoded string
        sh.send_data(conn, answer_json.encode())
    else:
        return 'shutdown'



def start(host, port):
     # Open socket
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        # Bind to host and port
        s.bind((host, port))
        # Listen for incoming connections
        s.listen()

        while True:
            # Accept incoming connections
            conn, addr = s.accept()
            # Handle the incoming connections
            command = handle_connection(conn, addr)
            
            # Close the connection
            conn.close()
            if command == 'shutdown':
                print("shutting down server")
                break
