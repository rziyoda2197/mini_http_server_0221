from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

server = HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)

print(f"Server running on http://localhost:{PORT}")
server.serve_forever()
