import socket

host  = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input("Enter a string  : ")

client_socket.sendto(message.encode(),(host,port))

response,server_address = client_socket.recvfrom(1024)
print(f"response got = reversed string : {response.decode()}")

client_socket.close()