import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    # print(message)

    if message == 'quit':
        client_socket.send('quit'.encode(ENCODER))
        print('\nEnding the chat')
        break
    else:
        print(f'\n{message}')
        message = input('Message: ')
        client_socket.send(message.encode(ENCODER))

client_socket.close()