import socket
import threading

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(message)

receiver_thread = threading.Thread(target = receive_messages)
receiver_thread.start()

while True:
    message = input("Client : ")
    client_socket.send(message.encode())

client_socket.close()