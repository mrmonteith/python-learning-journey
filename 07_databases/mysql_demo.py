#!/usr/bin/env python3
import os
from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

def get_users():
    conn = MySQLdb.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        passwd=os.getenv("MYSQL_PASSWORD", ""),
        db=os.getenv("MYSQL_DB", "python_learning")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    results = cursor.fetchall()
    conn.close()
    return [row[0] for row in results]

@app.route("/")
def index():
    users = get_users()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



# mysql_demo.py
# A simple Flask application that connects to a MySQL database
# and retrieves user data to display on a web page.
# The database connection parameters are read from environment variables.
# Make sure to set the following environment variables before running:
# MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
# Example:
# export MYSQL_HOST=localhost
# export MYSQL_USER=root
# export MYSQL_PASSWORD=stinky10
# export MYSQL_DB=python_learning
# The application assumes there is a table named 'users' with a column 'name'.
# The HTML template 'users.html' should be created in the 'templates' directory.
# Example content for 'users.html':
# <!doctype html>
# <html lang="en">
#   <head>
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1,
#     <title>User List</title>
#   </head>

#   <body>
#     <h1>Users</h1>
#     <ul>
#       {% for user in users %}
#         <li>{{ user }}</li>
#       {% endfor %}
#     </ul>
#   </body>
# </html>   

            