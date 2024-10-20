import socket
import threading

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Allow up to 5 connections

print(f"Server listening on {host}:{port}")

clients = []  # List to keep track of all connected clients

# Function to handle each client's communication
def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                print(f"{client_address} disconnected")
                clients.remove(client_socket)  # Remove client from the list
                broadcast(f"{client_address} has left the chat!".encode(), client_socket)
                client_socket.close()
                break
            else:
                print(f"Client {client_address}: {message}")
                broadcast(f"Client {client_address}: {message}".encode(), client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast messages to all connected clients except the sender
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:  # Send to everyone except the sender
            try:
                client.send(message)
            except:
                # Handle broken connection issues
                clients.remove(client)
                client.close()

# Function to allow server admin to send messages
def server_broadcast():
    while True:
        message = input("Server: ")
        if message.lower() == "exit":
            print("Server is shutting down...")
            broadcast("Server has disconnected.".encode())  # Notify all clients
            for client in clients:
                client.close()  # Close all client connections
            server_socket.close()
            break
        broadcast(f"Server: {message}".encode())  # Broadcast server's message to all clients

# Main loop to accept clients
def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)  # Add client to the list
        broadcast(f"{client_address} has joined the chat!".encode(), client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

# Start the client acceptance thread
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()

# Start the server message thread
server_broadcast()
