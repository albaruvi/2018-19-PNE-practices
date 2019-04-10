import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        msg = self.requestline

        msg_split = msg.split(' ')
        if msg_split[1] == ' ':
            filename = open('main-page.html', 'r')
            contents = filename.read()
        elif msg_split[1] == '/' or msg_split[1] == '/echo':
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

            status_line = 'HTTP/1.1 200 ok\r\n'

            header = 'Content-Type: text/html\r\n'
            header += 'Content-Length: {}\r\nº'.format(len(str.encode(content)))

            contents = status_line + header + '\r\n' + content
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