import socket
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

pt = input("Enter a plain text : ")
client_socket.sendto(pt.encode(),(host,port))

d = input("Enter the depth : ")
client_socket.sendto(d.encode(),(host,port))

message,server_address = client_socket.recvfrom(1024)
ct = message.decode()

print(f"Cipher text = {ct}")

client_socket.close()
