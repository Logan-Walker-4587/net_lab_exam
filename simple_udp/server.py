import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

print(f"Server listening on {host}:{port}")

message,client_address = server_socket.recvfrom(1024)

print(f"Received message = {message.decode()}")

response = "message received".encode()
server_socket.sendto(response,client_address)

server_socket.close()
