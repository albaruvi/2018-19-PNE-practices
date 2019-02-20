import socket
from P1.Seq import Seq

PORT = 8080
IP = '212.128.253.66'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    msg = cs.recv(2048).decode('utf-8')

    print('Message from the client: {}'.format(msg))

    s1 = Seq(msg)
    if 'len' in s1:
        msg = s1.len()
    elif 'reverse' in s1:
        msg = s1.reverse()


    # Sending the message back to the client
    # (because we are an echo server)
    cs.send(str.encode(msg))

    cs.close()


# Create a socket for connecting to the clients+
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready: {}'.format(serversocket))


while True:

    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print('Attending client: {}'.format(address))

    process_client(clientsocket)

    # Close the socket
    clientsocket.close()
