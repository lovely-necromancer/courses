"""Serve this folder and open the viewer. Usage: python3 run.py"""
import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store"); super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 8000), H) as s:
    url = "http://127.0.0.1:8000/index.html"; print("Serving", url, "(Ctrl+C to stop)")
    webbrowser.open(url); s.serve_forever()
