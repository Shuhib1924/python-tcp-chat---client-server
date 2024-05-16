import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto('hello server'.encode('utf-8'), (socket.gethostbyname(socket.gethostname()), 12345))