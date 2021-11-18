#from src.jsonhandler import json_handler as json
#from src.sockethandler import socket_handler as sh
#import socket as sock #lol
from tkinter import *

root = Tk()
root.title('CSC 532 Calculator')
root.config(bg = "blue")


def clickCalButton():
    # this is where it it would call to calculate
    print = Label(root, text='Calculating').grid(row=4, column=0)


# def read_file(file_path):
#     # Open file

#         # Read the file line by line and append to list 
#         # after removing trailing whitespace

#     # Return list
    



# def start(host, port):

#     # Read file from file path

#     # Convert the list to json

#     # Open TCP socket

#         # Connect to Host on port

#         # Send the json encoded as UTF-8 string

#         # Send the socket a shutdown message that this side of the 
#         # socket will not send any more data and will
#         # only listen for a reply
    

#         # Receive data


from src.calculator import calculator as calc
from src.sockethandler import socket_handler as sh
import socket as sock
from src.jsonhandler import json_handler as json




# def handle_connection(conn, addr):
#     # Receive data

#     # Convert received data from json string to list

#     # Calculate the answers from the list

#     # Convert the answer list to a json string

#     # Send the data over the socket as a UTF-8 encoded string




# def start(host, port):
#     # Open socket

#         # Bind to host and port

#         # Listen for incoming connections
     
#         # While true

#             # Accept incoming connections

#             # Handle the incoming connections

#             # Close the connection


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
    # with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
    #     s.connect((host, port))
    #     sh.send_data(s, file_json.encode())
    #     s.shutdown(sock.SHUT_WR)
    #     message = sh.receive_data(s)
    # print('message received: ', message)


    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.connect((host, port))
        shutdown_server(s)

title = Label(root, text='CSC 532 Calculator').grid(row=0, column=0)
demand = Label(root, text='Enter a calculation').grid(row=1, column=0)
inputfeild = Entry(root).grid(row =2, column = 0)
calbutton = Button(root, text="Calculate" , padx=50, command= clickCalButton).grid(row=3, column=0)

root.mainloop()




