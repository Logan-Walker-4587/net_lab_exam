import socket
import threading

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5) 
clients = []

def handle_clients(client_socket,client_address):
    while True: 
        message = client_socket.recv(1024).decode()
        print(f"Client {client_address} : {message}")
        broadcast(f"Client {client_address}: {message}".encode(),client_socket)

def broadcast(message,sender_socket = None):
    for client in clients:
        if client!=sender_socket:
            client.send(message)

def server_broadcast():
    while True :
          message = input("Server : ")
          broadcast(f"Server : {message}".encode())

def accept_client():
    while True:
        client_socket,client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target = handle_clients , args= (client_socket,client_address))
        thread.start()

accept_thread = threading.Thread(target = accept_client)
accept_thread.start()

server_broadcast()

