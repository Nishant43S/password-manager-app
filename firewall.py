import socket
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

# List of blocked IPs
BLOCKED_IPS = ['192.168.0.100', '10.0.0.50']

# Blocked request patterns (for example, SQL injection attempts or malicious URLs)
BLOCKED_PATTERNS = [r"SELECT.*FROM", r"DROP.*TABLE", r"<script.*>"]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get client IP
        client_ip = self.client_address[0]
        
        # Check if the IP is blocked
        if client_ip in BLOCKED_IPS:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"403 Forbidden: Your IP is blocked.")
            return

        # Check for any blocked patterns in the request path
        for pattern in BLOCKED_PATTERNS:
            if re.search(pattern, self.path, re.IGNORECASE):
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"403 Forbidden: Malicious request detected.")
                return

        # If no issues, proceed with the request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Welcome to the website!")

    def do_POST(self):
        # Handle POST requests in the same way
        self.do_GET()

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting simple firewall server on port {port}...')
    httpd.serve_forever()


