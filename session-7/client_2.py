# Programming our first client

import socket

# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')
PORT = 8080
IP = '212.128.253.64'

condition = True
while condition:
    # Connect to the server
    s.connect((IP, PORT))
    message = input('Please enter the message you want to send to the server')
    s.send(str.encode(message))

    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER:')
    print(msg)

    s.close()
    option = input('Do you want to continue sending messages?')
    if option == 'no':
        condition = False

print('the end')
