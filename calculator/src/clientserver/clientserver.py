from src.jsonhandler import json_handler as json
from src.sockethandler import sockethandler as sockhandler
import socket as sock
import concurrent.futures


HOST = '127.0.0.1'

PORT1 = 64000
PORT2 = 64001

message_list = []






# # Args is an array containing a port and a list
# def threaded_socket(args):
#     # Covert the list from args to a json string and then encode as a UTF-8 string
    

#     # Open a socket

#         # Connect to host on port from args

#         # Send the data
        
#         # Send the socket a shutdown message that this side of the 
#         # socket will not send any more data and will
#         # only listen for a reply

#         # Receive the data

#         # Convert the received data from a json string to a list

#         # Append the list to a global lists





# def handle_connection(conn, addr):

#     # Receive the data

#     # Convert the received data from a json string to a list


#     # Divide the list into two

#     # Create a ThreadPoolExecutor with 2 workers to call threaded socket
#     # with the port number of the receiving socket and half of the list 
#     # as arguments formatted as a tuple, e.g. (port, list)

#     # Combine the lists received from the server as a response into a single list
    
#     # Convert that list into a json string

#     # Send the list to the client as a UTF-8 encoded string






# def start(port):
#     # Open socket

#         # Bind to host and port

#         # Listen for incoming connections
     
#         # While true

#             # Accept incoming connections

#             # Handle the incoming connections

#             # Close the connection

