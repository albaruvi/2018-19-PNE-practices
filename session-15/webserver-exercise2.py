import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8002


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path.startswith('/main') or self.path == '/':
            filename = open('main-page2.html', 'r')
            contents = filename.read()
        elif self.path.sartswith('/echo'):
            msg_split = self.path.split('=')
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
            if 'on' in msg_split:
                contents += msg_split[1].upper()
            else:
                contents += msg_split[1]

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

