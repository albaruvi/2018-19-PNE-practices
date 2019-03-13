import socket

# SERVER IP, PORT
PORT = 8081
IP = '192.168.1.68'

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Before connecting to the server enter the string
msg = """
"""

# Now we can create the socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers responses
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))

s.close()
