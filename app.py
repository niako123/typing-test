from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)

app.config("TEMPLATES_AUTO_RELOAD") = True

@app.route("/")
def configuration():
    """ Guest configuration of the race """

    return "<p>Hello, World!</p>"

@app.route("/<username>")
def user_configuration():
    """ Users configuration of the race """

    return "TODO"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

@app.route("/register")
def register():
    return "TODO"

