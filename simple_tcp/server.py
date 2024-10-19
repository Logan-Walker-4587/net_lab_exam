import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))

server_socket.listen(1)
print(f"server listening on {host}:{port}")

client_socket,client_address = server_socket.accept()

message = client_socket.recv(1024).decode()

print(f"Received message from {client_address} : {message}")

response = "Message received"

client_socket.send(response.encode())

client_socket.close()
server_socket.close()

