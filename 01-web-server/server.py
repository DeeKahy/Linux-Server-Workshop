import http.server
import socketserver

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on http://0.0.0.0:{PORT}")
    print("Visit http://YOUR_SERVER_IP:8080 in your browser")
    print("Press ctrl+c to stop")
    httpd.serve_forever()
