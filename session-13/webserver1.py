import http.server
import socketserver

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print('GET received')

        print('Request line:' + self.requestline)
        print('  Cmd:  ' + self.command)
        print('  Path:  ' + self.path)

        content = 'I am the happy server'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(str.encode(content)))

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Serving at PORT', PORT)

    httpd.serve_forever()
