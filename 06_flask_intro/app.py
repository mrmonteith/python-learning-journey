#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        msg = request.form.get("message")
        message = f"Thanks {name}! We received your message: \"{msg}\" (we'll reply to {email})."
    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# To run the app, use the command:
# python3 app.py

# Then navigate to http://localhost:5000/ in your web browser.
# You should see the home page. Click on the link to go to the about page.
# http://127.0.0.1:5000/about → About page.

