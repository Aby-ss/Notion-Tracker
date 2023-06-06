import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Server has disconnected
            client_socket.close()
            break

def start_client():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Prompt user for a nickname
    nickname = input("Enter your nickname: ")
    client_socket.send(nickname.encode('utf-8'))

    # Start a new thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        # Send message to server
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == '__main__':
    start_client()
