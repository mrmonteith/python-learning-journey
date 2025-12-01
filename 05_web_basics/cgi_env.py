#!/usr/bin/env python3
import os

print("Content-Type: text/html\n")
print("<html><body><h2>CGI Environment Variables</h2><ul>")

for key, value in os.environ.items():
    print(f"<li>{key}: {value}</li>")

print("</ul></body></html>")
