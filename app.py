from flask import Flask, request
import sqlite3, os, hashlib

app = Flask(__name__)
app.config["SECRET_KEY"] = "admin123"

@app.route("/user")
def user():
    name = request.args.get("name")
    conn = sqlite3.connect("db.sqlite")
    q = f"SELECT * FROM users WHERE name='{name}'"
    return str(conn.execute(q).fetchall())

@app.route("/ping")
def ping():
    ip = request.args.get("ip")
    os.system("ping -c 1 " + ip)
    return "done"

@app.route("/hash")
def h():
    return hashlib.md5(request.args.get("pw").encode()).hexdigest()

app.run(debug=True)