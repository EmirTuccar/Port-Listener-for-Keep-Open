import socket

def start_listener(host, port):
    # Create a socket object
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to a specific address and port
        listener_socket.bind((host, port))
        
        # Listen for incoming connections
        listener_socket.listen(1)
        print(f"Listening on {host}:{port}")
        
        while True:
            # Accept a new connection
            client_socket, client_address = listener_socket.accept()
            print(f"Accepted connection from {client_address}")
            
            # Receive and process data from the client
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received data: {data}")
            
            # Respond to the client
            response = "Hello, client! Your message was received."
            client_socket.send(response.encode('utf-8'))
            
            # Close the client socket
            client_socket.close()
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the listener socket
        listener_socket.close()

if __name__ == "__main__":
    host = "192.168.56.101"  # Listen on all available interfaces
    port = 8080   # Choose a port number
    start_listener(host, port)
