import socket
import termcolor

PORT = 8081
IP = '212.128.253.69'
MAX_OPEN_REQUEST = 5

msg_client = []

def process_client(cs):
    """Process the client request.
        Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    msg_client.append(msg)

    # Print the received message, for debugging
    termcolor.cprint("Request message: {}".format(msg), 'green')

    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()

# MAIN PROGRAM
# Create a socket for connecting to the clients+
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready: {}'.format(serversocket))

status = True
while status:

    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print('Attending client: {}'.format(address))

    process_client(clientsocket)

    # Close the socket
    clientsocket.close()

    if 'EXIT' in msg_client:
        status = False
