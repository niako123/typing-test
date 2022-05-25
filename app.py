from flask import Flask, request, redirect, render_template, session, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

app = Flask(__name__)

# Configurations
app.secret_key = 'b1b92f2cd885248e85ba872c3399628d7062bf375d58fa0042f95afaf62a318e'

@app.route("/", methods=["GET", "POST"])
def configuration():
    """ Guest configuration of the race """

    error = None
    if request.method == "POST":
        configuration = request.form.get("configuration")

        if not configuration:
            error = "Select one of the configuration methods"
        elif configuration == "Configure time":
            flash('You were succesfully redirected')
            return render_template("limited.html")
        elif configuration == "Configure length":
            flash('You were succesfully redirected')
            return render_template("unlimited.html")
    return render_template("configuration.html", error=error)

@app.route("/register")
def register():
    return "TODO"

