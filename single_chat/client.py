import socket 
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

print(f"Connected to server at {host}:{port}")

while True:
    message = input("Client : ")
    if message.lower() == "exit":
        print("Client disconnected")
        break 
    else:
        client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()

    if response.lower() == "exit":
        print("server disconnected")
        break 
    else:
        print(f"Server : {response}")

client_socket.close()
