# Client for practice 2

import socket
from P1.Seq import Seq

# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')
PORT = 8080
IP = '212.128.253.66'

while True:
    sequence = Seq(input('Introduce a sequence:  '))

    complement = sequence.complement()
    reverse = sequence.reverse()
    # Connect to the server
    s.connect((IP, PORT))
    s.send(str.encode('The complement of the sequence is: {}'.format(complement)))
    s.send(str.encode('\n'))
    s.send(str.encode('The reverse of the sequence is: {}'.format(reverse)))
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER:')
    print(msg)

    s.close()
