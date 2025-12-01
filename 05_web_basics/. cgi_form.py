#!/usr/bin/env python3
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form.getvalue("name", "World")

print("<html>")
print("<head><title>CGI Form Demo</title></head>")
print("<body>")
print(f"<h1>Hello, {name}!</h1>")
print("</body>")
print("</html>")
