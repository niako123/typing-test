from flask import Flask, request, redirect, render_template, session, url_for, flash, g, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from random import randrange
import sqlite3
from random import shuffle
import numpy as np
import json
from flask_assets import Environment, Bundle
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
assets = Environment(app)

# Javascript code all together
js1 = Bundle('words.js', 'myscripts.js')
assets.register('js_1', js1)

js2 = Bundle('myscript2.js')
assets.register('js_2', js2)

# Session Configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

# Configurations
app.secret_key = 'b1b92f2cd885248e85ba872c3399628d7062bf375d58fa0042f95afaf62a318e'

@app.route("/", methods=["GET", "POST"])
def configuration():
    """ Guest configuration of the race """
    user = "guest"
    if 'user_id' in session:
        user = "user"
    if request.method == "POST":
        configuration = request.form.get("configuration")

        if configuration == "unlimited":
            flash('You were succesfully redirected')
            return render_template("unlimited.html")
        elif configuration == "limited":
            flash('You were succesfully redirected')
            return render_template("limited.html")
    return render_template("configuration.html", user=user)

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
        usernames = cur.execute("SELECT username FROM users WHERE id = ?", (session['user_id'], ))
        con.commit()
        for username in usernames:
            flash("Type to start.")
            return render_template("keyboard.html", player=username[0], seconds=seconds, minutes=minutes, user="user")

@app.route("/limited", methods=["POST"])
def text():
    """ Configure with an api """

    with sqlite3.connect('typer.db') as con:
        cur = con.cursor()
        if not 'user_id' in session:
            cur.execute('INSERT INTO requests (user, configuration) VALUES  (?, ?)', ("guest", "text length"))
            con.commit()
            flash("Type to start.")
            return render_template("keyboard_2.html", player="GUEST")
        cur.execute('INSERT INTO requests (user, configuration) VALUES  (?, ?)', (session["user_id"], "text length"))
        usernames = cur.execute("SELECT username FROM users WHERE id = ?", (session['user_id'], ))
        con.commit()
        for username in usernames:
            flash("Type to start.")
            return render_template("keyboard_2.html", player=username[0], user="user")

@app.route("/result", methods=["POST", "GET"])
def result():
    """ Show run history """

    if request.method == "POST":
        data = json.loads(request.data)
        min = data['min']
        sec = data['sec']
        speed = data['speed']
        configuration = data['configuration']

        with sqlite3.connect('typer.db') as con:
            cur = con.cursor()
            if not 'user_id' in session:
                if configuration == "text":
                    cur.execute('INSERT INTO runs (user, configuration, minutes, seconds, speed) VALUES  (?, ?, ?, ?, ?)', ("guest", "text length", min, sec, speed))
                else:
                    cur.execute('INSERT INTO runs (user, configuration, minutes, seconds, speed) VALUES  (?, ?, ?, ?, ?)', ("guest", "time limit", min, sec, speed))
                con.commit()
                return  jsonify(dict(redirect='/history'))
            usernames = cur.execute("SELECT username FROM users WHERE id = ?", (session['user_id'], ))
            for username in usernames:
                if configuration == "text":
                    cur.execute('INSERT INTO runs (user, configuration, minutes, seconds, speed) VALUES  (?, ?, ?, ?, ?)', (username[0], "text length", min, sec, speed))
                else:
                    cur.execute('INSERT INTO runs (user, configuration, minutes, seconds, speed) VALUES  (?, ?, ?, ?, ?)', (username[0], "time limit", min, sec, speed))
                con.commit()
                return  jsonify(dict(redirect='/history'))
    
@app.route("/history", methods=["GET"])
def history():
    """ Getting the page """
    runs = []
    user = ""
    username = ""
    with sqlite3.connect('typer.db') as con: 
        cur = con.cursor()
        if 'user_id' in session:
            usernames = cur.execute('SELECT username FROM users WHERE id = ?', (session['user_id'], ))
            for usernam in usernames:
                username = usernam[0]
            user = "user"
        else:
            user = "guest"
        runs = cur.execute('SELECT * FROM runs')
        con.commit()
        return render_template("history.html", user=user, runs=runs, username=username)


@app.route("/login", methods=['POST', 'GET'])
def login():
    """ Login into a username """
    rows = []
    if request.method == "POST":
        if not request.form.get('username'):
            return render_template("login.html", error="Must provide username")
        elif not request.form.get('password'):
            return render_template('login.html', error="Must provide password")

        with sqlite3.connect('typer.db') as con:
            cur = con.cursor()
            rows = cur.execute('SELECT * FROM users WHERE username = ?', (request.form.get('username'), ))
            con.commit()
        
        counter = 1
        for row in rows:
            if counter != 1 or not check_password_hash(row[2], request.form.get('password')):
                print(counter)
                return render_template("login.html", error='Invalid username and/or password')
            counter = counter + 1
            session['user_id'] = row[0]
        return redirect('/')
        
    return render_template("login.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    """ Register a new account """
    if request.method == "POST":
        session.clear()

        password = request.form.get("password")
        username = request.form.get("username")
        confirmation = request.form.get("confirmation")
        users = []
        user_id = []
        with sqlite3.connect('typer.db') as con: 
            cur = con.cursor()
            users = cur.execute('SELECT * FROM users')
            con.commit()
        
        # Ensure username and password were submitted
        if not username:
            return render_template("register.html", error="Missing username")
        if not password:
            return render_template("register.html", error="Missing password")
        if not confirmation:
            return render_template("register.html", error="Missing password confirmation")

        # check if username already exist
        for user in users:
            if username == user[1]:
                return render_template('register.html', error="Username already exist")
        
        # check for password twice
        if password != confirmation:
            return render_template('register.html', error='Passwords don\'t match')

        # submit the new user
        with sqlite3.connect('typer.db') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO users (username, hash) VALUES(?, ?)', (username, generate_password_hash(password)))
            user_id = cur.execute('SELECT id FROM users WHERE username = ?', (username,))
            con.commit()

        # start a session
        for user in user_id:
            session['user_id'] = user[0]
            return redirect("/")
    return render_template("register.html")


@app.route('/logout')
def logout():
    """Log user out"""
    session.clear()
    return redirect('/')