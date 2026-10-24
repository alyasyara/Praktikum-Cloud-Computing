from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "Hello from Cloud Computing Milestone 03 - Alya Syara Shafira!"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
