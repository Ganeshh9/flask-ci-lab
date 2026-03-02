from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Ganesh CI/CD LAb!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/slow")
def slow():
    time.sleep(3)
    return "Slow response simulated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
