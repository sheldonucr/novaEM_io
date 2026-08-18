#!/usr/bin/env python3
"""Minimal static file server for the MetalStack site.

Serves an absolute directory and never calls os.getcwd(), so it works even
when the process's working directory is on a restricted/external mount where
`python -m http.server` crashes with PermissionError on os.getcwd().
"""
import socketserver
from functools import partial
from http.server import SimpleHTTPRequestHandler

DIRECTORY = "/Volumes/joule/novaEM_io"
PORT = 8000


class Server(socketserver.TCPServer):
    allow_reuse_address = True


def main():
    handler = partial(SimpleHTTPRequestHandler, directory=DIRECTORY)
    with Server(("", PORT), handler) as httpd:
        print(f"Serving {DIRECTORY} at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
