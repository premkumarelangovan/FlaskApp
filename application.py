from flask import Flask
application = Flask(__name__)


@application.route("/")
def home():
    return "Hello World, from Flask!"


if __name__ == "__main__":
    application.run()

