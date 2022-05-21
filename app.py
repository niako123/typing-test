from flask import Flask, request, redirect, render_template, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def configuration():
    """ Guest configuration of the race """
    if request.method == "POST":
        return "<p>Hello, World!<p>"
    else:
        return render_template("configuration.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

@app.route("/register")
def register():
    return "TODO"

