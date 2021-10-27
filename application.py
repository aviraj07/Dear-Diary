import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

@app.route("/")
@login_required
def index():
    user_data = db.execute("SELECT date, subject FROM data WHERE user_id = ?",session["user_id"])
    return render_template("index.html",user_data=user_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Invalid username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM user_info WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        rows = db.execute("SELECT * FROM user_info WHERE username = ?",username)

        if not username:
            return apology("Invalid username",400)
        elif len(rows) != 0:
            return apology("username exists",400)
        elif not password:
            return apology("Invalid passowrd",400)
        elif not confirmation:
            return apology("Provide the confirmation password",400)
        elif not password == confirmation:
            return apology("Passwords do not match",400)
        else:
            hash_pass = generate_password_hash(password)
            db.execute("INSERT INTO user_info (username,hash) VALUES (?,?)",username,hash_pass)
            return redirect("/login")

    else:
        return render_template("register.html")



@app.route("/new",methods=["GET","POST"])
def new():

    if request.method == "POST":
        subject = request.form.get("subject")
        content = request.form.get("content")

        db.execute("INSERT INTO data (user_id,writeup,subject,date) VALUES (?,?,?,?)",session["user_id"],content,subject,formatted_date)

        return redirect("/")

    else:
        return render_template("new.html")

@app.route("/content",methods=["GET","POST"])
def content():
    if request.method == "POST":
        return redirect("/")

    else:
        date = request.form.get("dat")
        contents = db.execute("SELECT writeup FROM data WHERE user_id = ? AND date = ?",session["user_id"],date)
        subject = db.execute("SELECT subject FROM data WHERE user_id = ? AND date= ?",session["user_id"],date)

        return render_template("content.html",contents=contents,subject=subject)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
