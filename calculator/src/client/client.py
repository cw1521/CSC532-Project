
# from tkinter import *
# import os
# from pathlib import Path

# root = Tk()
# root.title('CSC 532 Calculator')
#root.config(bg = "blue")
#root.geometry('160x150')


# def clickCalButton():
#     # this is where it it would call to calculate
#     print = Label(root, text='Calculating').pack()



# def open_file():

#     with os.scandir('test/src/') as entries:
#         for entry in entries:
#             if entry.is_file():
#                 print(entry.name)




from src.jsonhandler import json_handler as json
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
    file_path = getcwd() + '/csc532-project/calculator/src/functions.txt'
    file_list = read_file(file_path)
    # print(file_list)

    file_json = json.get_json_from_list(file_list)
    # print(file_json)

    message = ''
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.connect((host, port))
        sh.send_data(s, file_json.encode())
        s.shutdown(sock.SHUT_WR)
        message = sh.receive_data(s)
    print('message received: ', message)




#title = Label(root, text='CSC 532 Calculator' , font=80).pack()
# demand1 = Label(root, text='Upload a file', font=16).pack()
# inputfeild1 = Entry(root).pack()
# btn = Button(root, text='Browse File Directory', padx=6, pady=6,font=16, command=lambda: open_file())
# btn.pack()
# demand = Label(root, text='Enter a problem', font=16).pack()
# inputfeild = Entry(root).pack()
# space = Label(root, text='                                                                                           ').pack()
# calbutton = Button(root, text="Calculate", font=16, command=clickCalButton).pack()

# root.mainloop()



