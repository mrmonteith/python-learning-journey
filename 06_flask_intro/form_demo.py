#!/usr/bin/env python3
from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Form Demo</title></head>
<body>
    <h1>Flask Form Demo</h1>
    <form method="post" action="/">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    {% if name %}
        <h2>Hello, {{ name }}!</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form_demo():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template_string(form_html, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# to run the app, use the command:
# python3 form_demo.py
# Then navigate to http://localhost:5000/ in your web browser.
# You should see a form where you can enter your name.
# After submitting the form, you should see a greeting with your name.
