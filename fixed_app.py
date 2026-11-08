from flask import Flask, request
import sqlite3, os, hashlib, subprocess

app = Flask(hassan)
app.config["secret"] = os.environ.get("SECRET_KEY", "change-me")

@app.route("/user")
def user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("db.sqlite")
    cur = conn.execute("SELECT * FROM users WHERE name=?", (name,))
    return str(cur.fetchall())

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "")
    if not ip.replace(".", "").isdigit():
        return "invalid ip"
    subprocess.run(["ping", "-n", "1", ip])
    return "done"

@app.route("/hash")
def h():
    pw = request.args.get("pw", "")
    return hashlib.sha256(pw.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=False)