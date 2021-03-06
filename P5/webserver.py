import http.server
import socketserver
import termcolor

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Print the received message, for debugging
        print()
        print("Request message: ")
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/pink':
            filename = open('pink.html', 'r')
            contents = filename.read()
        elif self.path == '/blue':
            filename = open('blue.html', 'r')
            contents = filename.read()
        elif self.path == '/' or self.path == '/index':
            filename = open('index.html', 'r')
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
