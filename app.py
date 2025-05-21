from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello from AWS EC2 Python App")

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server listening on port 8080")
    httpd.serve_forever()
