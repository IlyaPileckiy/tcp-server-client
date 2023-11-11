from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode("utf-8")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("This is POST request. ", "utf-8"))
        self.wfile.write(bytes("Received: ", "utf-8"))
        self.wfile.write(bytes(body, "utf-8"))
        print(body)

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
