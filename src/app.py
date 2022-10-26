from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, first test of deploying app using GitHub Actions"

if __name__== "__main__":
    app.run()
