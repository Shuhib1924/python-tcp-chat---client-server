import socket
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print('Server is running...\n')
client_socket, client_address = server_socket.accept()
client_socket.send('you are connected to the server...\n'.encode(ENCODER))