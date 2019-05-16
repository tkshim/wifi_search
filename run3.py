#!/usr/bin/env python3
import http.server

server_address = ("", 8000)
handler_class = http.server.CGIHTTPRequestHandler #set handler
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()
