import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# before decoding
message = client_socket.recv(1024)
print(message)
print(type(message))

# after decoding
message = message.decode('utf-8')
print(message)
print(type(message))