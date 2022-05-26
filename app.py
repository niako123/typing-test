from flask import Flask, request, redirect, render_template, session, url_for, flash, g
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from random import randrange
import time
import sqlite3

app = Flask(__name__)

# Configurations
app.secret_key = 'b1b92f2cd885248e85ba872c3399628d7062bf375d58fa0042f95afaf62a318e'

# Open a file for the directionary
f = open("words.txt")
words = f.readlines()
f.close()

@app.route("/", methods=["GET", "POST"])
def configuration():
    """ Guest configuration of the race """

    if request.method == "POST":
        configuration = request.form.get("configuration")

        if configuration == "Configure time":
            flash('You were succesfully redirected')
            return render_template("limited.html")
        elif configuration == "Configure length":
            flash('You were succesfully redirected')
            return render_template("unlimited.html")
    return render_template("configuration.html")

@app.route("/register")
def register():
    return "TODO"

@app.route("/limited", methods=["POST"])
def time():
    """ Configure with dictionary """

    minutes = request.form.get("minutes")
    seconds = request.form.get("seconds")

    if not seconds and not minutes:
        return render_template("limited.html", error="Invalid: choose valid values")
    if not seconds:
        seconds = 0
    if not minutes: 
        minutes = 0

    minutes = int(minutes)
    seconds = int(seconds)
    with sqlite3.connect('typer.db') as con:
        cur = con.cursor()
        if not 'user_id' in session:
            cur.execute('INSERT INTO requests (minutes, seconds, user) VALUES (?, ?, ?, ?)', (minutes, seconds, "guest", "time limit"))
            con.commit()
            return render_template("keyboard.html", player="GUEST")
        cur.execute('INSERT INTO requests (minutes, seconds, user) VALUES (?, ?, ?, ?)', (minutes, seconds, session['user_id'], "time limit"))
        con.commit()
        return TODO