import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

message = "hello"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Response from server = {response}")

client_socket.close()


