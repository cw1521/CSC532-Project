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


title = Label(root, text='CSC 532 Calculator').grid(row=0, column=0)
demand = Label(root, text='Enter a calculation').grid(row=1, column=0)
inputfeild = Entry(root).grid(row =2, column = 0)
calbutton = Button(root, text="Calculate" , padx=50, command= clickCalButton).grid(row=3, column=0)

root.mainloop()



