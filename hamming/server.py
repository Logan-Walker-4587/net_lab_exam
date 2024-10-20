import socket 
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))

print(f"Server listening on {host}:{port}")
server_socket.listen()
client_socket,client_address = server_socket.accept()

hm_code = client_socket.recv(1024).decode()
print(f"Hamming code received : {hm_code}")

response = "correct code"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()