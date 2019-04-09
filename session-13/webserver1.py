import http.server
import socketserver

# Define the Server's port
PORT = 8000

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    httpd.serve_forever()
