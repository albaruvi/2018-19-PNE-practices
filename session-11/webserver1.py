import socket
import termcolor

IP = "192.168.1.68"
PORT = 8082

MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    content = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Green server</title>
      </head>
      <body style="background-color: green;">
        <h1>GREEN SERVER</h1>
        <p>I am the Green Server! :-)</p>
      </body>
    </html>
    """
    
    # Everything is ok
    status_line = 'HTTP/1.1 200 ok\r\n'

    header = 'Content-Type: text/html\r\n'
    header += 'Content-Length: {}\r\nº'.format(len(str.encode(content)))

    response_msg = status_line + header + '\r\n' + content

    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
