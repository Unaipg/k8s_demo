import os 
import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(f"Hello {os.environ.get('username')}".encode("utf-8"))


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
