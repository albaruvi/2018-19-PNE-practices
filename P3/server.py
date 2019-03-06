import socket

PORT = 8081
IP = '212.128.253.69'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    msg = cs.recv(2048).decode('utf-8')

    print('Message from the client: {}'.format(msg))

    msg_split = msg.split('\n')

    if msg_split[0] == '':
        response = str.encode('ALIVE')
        cs.send(response)
        cs.close()
        return
    elif msg_split[0] != '':
        for i in msg_split[0].lower():
            if i != 'a' and i != 't' and i != 'c' and i != 'g':
                response = 'ERROR'
                response1 = str.encode(response)
                cs.send(response1)
                cs.close()
                return
            else:
                response = str.encode('OK\n')
                cs.send(response)
                cs.close()
                return



    # Sending the message back to the client
    # (because we are an echo server)



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
