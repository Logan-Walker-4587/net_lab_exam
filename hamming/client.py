import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

data = input("Enter dataword : ")
d = []
for i in range(len(data)):
    d.append(int(data[i]))

p0 = d[3] ^ d[2] ^ d[0]
p1 = d[3] ^ d[1] ^ d[0]
p2 = d[2] ^ d[1] ^ d[0]

hamming_code = [d[0],d[1],d[2],p2,d[0],p1,p0]

hm_code = []
for i in range(len(hamming_code)):
    hm_code.append(str(hamming_code[i]))

codeword = "".join(hm_code)


client_socket.send(codeword.encode())

reply = client_socket.recv(1024).decode()
print(f"response = {reply}")

client_socket.close()