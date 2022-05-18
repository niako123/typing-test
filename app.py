from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def configuration():
    """ Guest configuration of the race """

    return "<p>Hello, World!</p>"

@app.route("/<username>")
def user_configuration():
    """ Users configuration of the race """

    return "TODO"

