import socket
import threading

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print(f"Connected to server at {host}:{port}")

# Function to handle receiving messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except:
            # If there's an error, close the socket and break the loop
            print("Disconnected from server")
            client_socket.close()
            break

# Start a thread to continuously receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input("You: ")
    if message.lower() == "exit":
        client_socket.send("exit".encode())
        print("You disconnected")
        break
    else:
        client_socket.send(message.encode())

client_socket.close()
