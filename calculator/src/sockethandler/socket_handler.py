import socket as sock


def send_data(socket, message):
    # Send message over socket
    socket.sendall(message)




def receive_data(socket):
    data_recv = b''
    # While true
    while True:
        # Receive data over socket in 1024 byte chunks
        data = socket.recv(1024)

        # Append each chunk to a byte string
        data_recv += data

        # If no data received break
        if not data:
            break

    # Return the decoded byte string in UTF-8 format
    return data_recv.decode()
