#!/usr/bin/python
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import time

PORT = 8080

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
    time.sleep(2)
print("Made using Edge Impulse")
    time.sleep(2)
print("Credits : Arijit Das, Jan Jongboom & Jeremy Ellis")
    time.sleep(2)
print("Wait until we setup everything for you")
    time.sleep(2)
print("serving at port ", PORT)
    time.sleep(2)
print("Visit http://localhost:8080/ to check out the live webserver")

httpd.serve_forever()
