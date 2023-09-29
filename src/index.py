"""
Simple HTTP Server

Run server: python3 index.py 10000
Access at: http://localhost:10000
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("Hello Python World", "utf8"))
    # end def do_GET

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length).decode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = "<pre>" + request_body + "</pre>"
        self.wfile.write(bytes(html, "utf8"))
    # end def do_POST
# end class RequestHandler

def run():
    host = "localhost"
    port = int(sys.argv[1]) if (len(sys.argv) > 1) else 10000

    server = HTTPServer((host, port), RequestHandler)
    print("Server started at http://%s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")
# end def run

run()
