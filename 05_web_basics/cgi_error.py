#!/usr/bin/env python3
print("Content-Type: text/html\n")

try:
    # Force an error for demo
    result = 10 / 0
    print(f"<p>Result: {result}</p>")
except Exception as e:
    print("<h2>Error occurred:</h2>")
    print(f"<pre>{e}</pre>")
