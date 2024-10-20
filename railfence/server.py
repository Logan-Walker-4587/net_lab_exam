import socket
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

plain_text,client_address = server_socket.recvfrom(1024)
plain_text = plain_text.decode()
print(f"Received plain text : {plain_text}")
depth,client_address = server_socket.recvfrom(1024)
depth = int(depth.decode())
print(f"Received Depth : {depth}")

count = 0
up = 0
fence = []
for _ in range(depth):
    fence.append([])

for i in range(len(plain_text)):
    fence[count].append(plain_text[i])
    if up ==0:
        count+=1
        if count == depth:
            count -= 1
            up = 1
    else:
        count -= 1
        if count == -1:
            up = 0
            count = 0

cipher_text = "".join("".join(row) for row in fence)
server_socket.sendto(cipher_text.encode(),client_address)

server_socket.close()
    

