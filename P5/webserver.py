import http.server
import socketserver
import termcolor

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        msg = self.requestline

        # Print the received message, for debugging
        print()
        print("Request message: ")
        termcolor.cprint(msg, 'green')

        msg_split = msg.split(' ')

        if msg_split[1] == '/pink':
            filename = open('pink.html', 'r')
            contents = filename.read()
        elif msg_split[1] == '/blue':
            filename = open('blue.html', 'r')
            contents = filename.read()
        elif msg_split[1] == '/' or msg_split[1] == '/index':
            filename = open('index-exercise-1.html', 'r')
            contents = filename.read()
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
