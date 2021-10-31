from src.jsonhandler import json_handler as json
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




# Args is an array containing a host, a port, and a list
def threaded_socket(args):
    # Covert the list from args to a json string and then encode as a UTF-8 string
    message = json.get_json_from_list(args[2]).encode()

    # Open a socket
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        # Connect to host on port from args
        s.connect((args[0], args[1]))

        # Send the data
        sh.send_data(s, message)

        # Send the socket a shutdown message that this side of the 
        # socket will not send any more data and will
        # only listen for a reply
        s.shutdown(sock.SHUT_WR)

        # Receive the data
        message = sh.receive_data(s)

        # Convert the received data from a json string to a list
        func_list = json.get_list_from_json(message)

        # Append the list to a global lists
        message_list.append(func_list)





def handle_connection(conn, addr):

    # Receive the data
    message = sh.receive_data(conn) 
    print('Received: ', message)
    # Convert the received data from a json string to a list
    func_list = json.get_list_from_json(message)
    print(func_list)
    # Divide the list into two
    i = len(func_list)//2

    # Create a ThreadPoolExecutor with 2 workers to call threaded socket
    # with the port number of the receiving socket and half of the list 
    # as arguments formatted as a tuple, e.g. (port, list)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(threaded_socket, [(SERVER1_HOST, SERVER1_PORT, func_list[0:i]), (SERVER2_HOST, SERVER2_PORT, func_list[i:len(func_list)])])
    
    # Combine the lists received from the server as a response into a single list
    answer = message_list[0] + message_list[1]

    # Convert that list into a json string
    answer_json = json.get_json_from_list(answer)
    
    # Send the list to the client as a UTF-8 encoded string
    print('Sending: ', answer_json)
    sh.send_data(conn, answer_json.encode())







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


    # Open socket
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        # Bind to host and port
        s.bind((host, port))
        

        # Listen for incoming connections
        s.listen()
        # While true
        while True:
            # Accept incoming connections
            conn, addr = s.accept()
            # Handle the incoming connections
            command = handle_connection(conn, addr)
            # Close the connection
            conn.close()
