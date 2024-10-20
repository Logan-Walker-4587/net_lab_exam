import socket
host='127.0.0.1'
port=13213

client_socket=socket.socket()
client_socket.connect((host,port))

print("client live")

while(True):

    msg=input("enter text:")
    client_socket.send(msg.encode())
    if(msg=="exit"):
        break;
  

        

client_socket.close()
print("Client closed.")


