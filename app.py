from flask import Flask, request, redirect, render_template, session, url_for, flash, g
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from random import randrange
import sqlite3
from random import shuffle
import numpy as np

app = Flask(__name__)

# Configurations
app.secret_key = 'b1b92f2cd885248e85ba872c3399628d7062bf375d58fa0042f95afaf62a318e'

@app.route("/", methods=["GET", "POST"])
def configuration():
    """ Guest configuration of the race """

    if request.method == "POST":
        configuration = request.form.get("configuration")

        if configuration == "unlimited":
            flash('You were succesfully redirected')
            return render_template("unlimited.html")
        elif configuration == "limited":
            flash('You were succesfully redirected')
            return render_template("limited.html")
    return render_template("configuration.html")

@app.route("/register")
def register():
    return "TODO"

@app.route("/unlimited", methods=["POST"])
def time():
    """ Configure with dictionary """

    minutes = request.form.get("minutes")
    seconds = request.form.get("seconds")

    if not seconds and not minutes:
        return render_template("unlimited.html", error="Invalid: choose valid values")
    if not seconds:
        seconds = 0
    if not minutes: 
        minutes = 0

    minutes = int(minutes)
    seconds = int(seconds)
    with sqlite3.connect('typer.db') as con:
        cur = con.cursor()
        if not 'user_id' in session:
            cur.execute('INSERT INTO requests (minutes, seconds, user, configuration) VALUES (?, ?, ?, ?)', (minutes, seconds, "guest", "time limit"))
            con.commit()
            flash("Type to start.")
            return render_template("keyboard.html", player="GUEST", seconds=seconds, minutes=minutes)
        cur.execute('INSERT INTO requests (minutes, seconds, user, configuration) VALUES (?, ?, ?, ?)', (minutes, seconds, session['user_id'], "time limit"))
        con.commit()
        return "TODO"

@app.route("/limited", methods=["POST"])
def text():
    """ Configure with an api """

    difficulty = request.form.get("difficulty")

    if difficulty == "Difficulty":
        return render_template("limited.html", error="Invalid: choose a valid option")

    with sqlite3.connect('typer.db') as con:
        if not 'user_id' in session:
            cur.execute('INSERT INTO requests (difficulty, user, configuration) VALUES  (?, ?, ?)', (difficulty, "guest", "text length"))
            con.commit()
            flash("Type to start.")
            return render_template("keyboard_2.html", player="GUEST", difficulty=difficulty)
        cur.execute('INSERT INTO requests (difficulty, user, configuration) VALUES  (?, ?, ?)', (difficulty, session["user_id"], "text length"))
        con.commit()
        flash("Type to start.")
        return "TODO"