import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = "hello server".encode()
client_socket.sendto(message,(host,port))

response, server_address = client_socket.recvfrom(1024)
print(f"response from server = {response.decode()}")

client_socket.close()

