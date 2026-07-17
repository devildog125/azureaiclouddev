from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "testing webhook test from mac"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

