from flask import Flask, request, jsonify
import sqlite3, os

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "data.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS messages (text TEXT)")

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    msg = data.get("text")
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO messages (text) VALUES (?)", (msg,))
    return jsonify({"status": "ok", "text": msg})

@app.route("/list")
def list_msgs():
    with sqlite3.connect(DB_PATH) as conn:
        msgs = [r[0] for r in conn.execute("SELECT text FROM messages")]
    return jsonify(msgs)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", 5000)))
