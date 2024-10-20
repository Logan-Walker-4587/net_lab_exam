import socket
import threading

def func(client_socket,client_address):
 while(True):
   try:
    msg=client_socket.recv(1024).decode()
    if(msg=="exit"):
        break;
    else:
        print(f"{msg}")
   except Exception as e:
        print(f"Error: {e}")
        break  
 client_socket.close()



host='127.0.0.1'
port=13213

server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen(1)


print("server live")
while True:
 client_socket,client_address=server_socket.accept()
 client_thread=threading.Thread(target=func,args=(client_socket,client_address))
 client_thread.start()





server_socket.close()


