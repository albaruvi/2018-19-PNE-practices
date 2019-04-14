import http.server
import socketserver
import termcolor
from P3.seqP3 import Seq
# Define the Server's port
PORT = 8002


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        msg = self.requestline

        msg_split = msg.split(' ')
        if msg_split[1].startswith('/main') or msg_split[1] == '/':
            filename = open('main-page.html', 'r')
            contents = filename.read()
        elif msg_split[1].startswith('/seq'):
            msg_split2 = msg_split[1].split('=')
            msg_split3 = []
            for i in msg_split2:
                msg_split3 += i.split('&')
            for i in msg_split3[1].lower():
                if i != 'a' and i != 't' and i != 'c' and i != 'g':
                    result = 'no'
                else:
                    result = 'yes'
            if result == 'no':
                filename = open('error.html', 'r')
                contents = filename.read()
            elif result == 'yes':
                contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>MSG</title>
                        </head>
                        <body>
                            <h1>Echoing the message received</h1>
                            <p> """
                contents += 'The sequence we are working with is: ' + msg_split3[1] + '<p>' + '\n' + '<p>'
                sequence = Seq(msg_split3[1])
                if 'on' in msg_split3:
                    l1 = sequence.len()
                    contents += 'Length of the sequence = ' + str(l1) + '<p>' + '\n' + '<p>'
                if 'count' in msg_split3:
                    # Count the number of the base selected in the sequence
                    base = msg_split2[-1]
                    count_bases = sequence.count_base()
                    base_requested = count_bases[base+'s']
                    contents += 'Number of ' + base + 's found = ' + str(base_requested) + '<p>' + '\n' + '<p>'
                if 'perc' in msg_split3:
                    # Calculates the percentage of the base selected in the sequence
                    base = msg_split2[-1]
                    percentages = sequence.perc_bases()
                    base_requested = percentages[base+'s']
                    contents += 'Percentage of ' + base + 's = ' + str(base_requested) + '<p>' + '\n' + '<p>'

                contents += """</p>
                                <a href="main-page">MAIN page</a>
    
                            </body>
                            </html>
                            """

        else:
            filename = open('error.html', 'r')
            contents = filename.read()

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header("Content-Type", "text/html\r\n")

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")