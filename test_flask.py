""" fait hello world dans un navigateur"""

from flask import Flask

app = Flask(__name__)

@APP.route("/")
def index():
    """ecrit hello world"""
    return "Hello World"

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
