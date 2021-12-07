

def send_data(socket, message):
    socket.sendall(message)

def receive_data(socket):
    data_recv = b''
    while True:
        data = socket.recv(1024)
        data_recv += data
        if not data:
            break
    return data_recv.decode()
