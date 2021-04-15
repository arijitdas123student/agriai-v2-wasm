import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8082

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map={
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.css': 'text/css',
    '.js': 'application/x-javascript',
    '.wasm': 'application/wasm',
    '': 'application/octet-stream', # Default
    }

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Welcome to AgriAI V2 Setup")
print("Made using Edge Impulse")
print("Credits : Arijit Das, Jan Jongboom")
print("Wait until we setup everything for you")
print("serving at port ", PORT)
print("Visit http://localhost:8082/ to check out the live webserver")

httpd.serve_forever()
