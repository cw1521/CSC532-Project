from src.calculator import calculator as calc
from src.sockethandler import sockethandler as sockhandler
import socket as sock
from src.jsonhandler import json_handler as json


HOST = '127.0.0.1' #loopback IPv4interface
PORT = 65432 
# port 1 -65535



def handle_connection(conn, addr):
#     # Receive data
    sock.connect((conn,addr))
    jsonData = ""
#     # Convert received data from json string to list
    dataList = json.loads(jsonData)
#     # Calculate the answers from the list
    calc(dataList)
#     # Convert the answer list to a json string
    # list(eq,ans)
    jsonStr = json.dumps(dataList)
    # turn list into json
    jsonStr.encoded()
#     # Send the data over the socket as a UTF-8 encoded string
    sock.send(jsonStr)



def start(port):
    with sock.sock(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen() # let's sever accept connections
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)# if empty client closed and loop done
                if not data:
                    break
                conn.sendall(data)



