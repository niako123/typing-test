# Typer Racer

## **Video Demo:** [Click Here](https://youtu.be/N_HKlm8VaW4)

## **Content:**

- Description
- Ideas when starting
- Files Content
- Designer Choices
- Skills acquired
- Copyrights

### ***Description***

The main idea is that it is a website made in flask which purpose is to track users speed by two different ways, and can be played as a guest. Either the user chooses to do a time limit game which displays a set of words until the time runs out, or a text length which was choosing randomly using an API (see contributions). In the end, the user is able to login, and register to play as a registered user which helps them track their average speed through all the games.

### ***Ideas when starting***

There were many ideas that I had for my project. Somewhere I did not have much knowledge, or even had an idea of how it is done. For example, I wanted to make a python game, but it didn't review of what I learned in CS50. Instead, I decided to make a website using flask. Flask consists of using different languages, not necessarily programming, such as Python, JavaScript, HTML, and CSS.

After choosing making a website, I started to think about what could be an interesting way to make it not only design based, but also user interactive. Furthermore, my choice to making a game, more specifically a typing game. The simple idea was to make the user interact with the website as much as possible.

Some of the ideas were to make a keyboard, a leaderboard, and a database of users with logins, yet still be accessible to guests. Also, I thought to add two types of games that the user could play with a typing game, a word only, or/and a quote. In the end I decided to include both.

### ***Files Content***

``Files made in Python``

1. **app.py**

This is the thing the runs my variables and redirect the user from one website page to another.

``Files made in JavaScript``

- **myscripts.js / myscript2.js**

Helps to change the innerhtml colour of words, calculate the speed and changes the time.

- **button_change.js**

Change the table in the history.html from general to users only and vice versa.

- **words.js**

A set of words put in an array, for the source see copyrights.

``Files made in HTML``

- **layout.html**

A layout for all the HTML present.

- **configuration.html**

The main menu, where the user chooses the game they would like to play (time limited or text limited).

- **history.html**

The database of all runs that were made. If the user is login, he can see two buttons. One which is the general who shows everyone's results, while the other one shows the user only results.

- **keyboard_2.html**

The layout of the game that we play for limited text.

- **keyboard.html**

The layout of the game that we play for limited timed (chosen by the user).

- **limited.html**

Where the user press a button to start the limited text game.

- **login.html**

Ask the username and password to start a session of an already existent user.

- **register.html**

Register a new user to the database.

- **unlimited.html**

Where the user enters a time desired to start the limited time game.

### ***Designer Choice***

In the whole beginning, when I was forming my ideas for I wanted to make an interactive keyboard. The idea was discarded because of the complexity of the task.

### ***Skills acquired***

- API usage (free resource)

- Make an array from a file (python to JavaScript)

- Better knowledge on JavaScript

- Use of AJAX and Flask together

- Use of Bootstrap for design

- Use of pipenv

### ***Copyrights***

&copy; Copyright 2022, Luke Peavey.

&copy; Copyright 2022, Unlicense.
