import socket

host  = '127.0.0.1'
port = 12345
reversed_str = []
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

print(f"server listening on {host}:{port}")

message,client_address = server_socket.recvfrom(1024)
input = message.decode()
for i in range(len(input)-1,-1,-1):
    reversed_str.append(input[i])

reversed_input = "".join(reversed_str)
response = reversed_input.encode()

server_socket.sendto(response,client_address)

server_socket.close()
