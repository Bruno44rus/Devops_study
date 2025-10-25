from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    with open("logs/app.log", "a") as f:
        f.write(f"Visited at {datetime.datetime.now()}\n")
    return "Log entry added! Check the logs folder."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
