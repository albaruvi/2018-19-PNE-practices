import socket
from P3.seqP3 import Seq

PORT = 8081
IP = '192.168.1.68'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    response = ''
    msg = cs.recv(2048).decode('utf-8')

    print('Message from the client: {}'.format(msg))

    msg_split = msg.split('\\n')
    print(msg_split)

    if msg_split[0] == '':  # First line empty
        response += 'ALIVE'
        cs.send(str.encode(response))
        cs.close()
        return
    elif msg_split[0] != '':
        for i in msg_split[0].lower():  # First line not valid
            if i != 'a' and i != 't' and i != 'c' and i != 'g':
                response += 'ERROR'
                response1 = str.encode(response)
                cs.send(response1)
                cs.close()
                return

        response += 'OK\n'
        sequence = Seq(msg_split[0])
        for i in msg_split:  # Checking all the lines one by one and adding the answer to response
            if i == 'len':
                l1 = sequence.len()
                response += str(l1) + '\n'
            if i == 'complement':
                comp = sequence.complement()
                response += comp + '\n'
            if i == 'reverse':
                reverse = sequence.reverse()
                response += reverse + '\n'
            if i == 'countA':
                count_bases = sequence.count_base()
                base_requested = count_bases['As']
                response += str(base_requested) + '\n'
            if i == 'countT':
                count_bases = sequence.count_base()
                base_requested = count_bases['Ts']
                response += str(base_requested) + '\n'
            if i == 'countG':
                count_bases = sequence.count_base()
                base_requested = count_bases['Gs']
                response += str(base_requested) + '\n'
            if i == 'countC':
                count_bases = sequence.count_base()
                base_requested = count_bases['Cs']
                response += str(base_requested) + '\n'
            if i == 'percA':
                percentages = sequence.perc_bases()
                base_requested = percentages['As']
                response += str(base_requested) + '%' + '\n'
            if i == 'percT':
                percentages = sequence.perc_bases()
                base_requested = percentages['Ts']
                response += str(base_requested) + '%' + '\n'
            if i == 'percG':
                percentages = sequence.perc_bases()
                base_requested = percentages['Gs']
                response += str(base_requested) + '%' + '\n'
            if i == 'percC':
                percentages = sequence.perc_bases()
                base_requested = percentages['Cs']
                response += str(base_requested) + '%' + '\n'

        cs.send(str.encode(response))  # Sending back the response to the client
        return

    # Sending the message back to the client

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

    clientsocket.close()
