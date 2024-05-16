import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ^ Get IP
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))


server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

server_socket.listen()