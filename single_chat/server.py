import socket 
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

client_socket,client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    message = client_socket.recv(1024).decode()
    if message.lower() == "exit":
        print("Client disconnected")
        break 
    else:
        print(f"Client : {message}")
    
    response = input("Server : ")

    if response.lower() == "exit":
        print("server disconnected")
        break 
    else:
        client_socket.send(response.encode())

client_socket.close()
server_socket.close()
    




    