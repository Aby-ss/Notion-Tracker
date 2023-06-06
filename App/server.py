import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

# List to store connected clients
clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')

            # Broadcast the message to all connected clients
            for client in clients:
                if client != client_socket:
                    client.send(f'{client_address[0]}: {message}'.encode('utf-8'))
        except:
            # Client has disconnected
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('Server started. Waiting for connections...')

    while True:
        # Accept client connection
        client_socket, client_address = server_socket.accept()

        # Add client to the list
        clients.append(client_socket)

        # Start a new thread to handle client communication
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == '__main__':
    start_server()