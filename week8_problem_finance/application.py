import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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


# Custom filter : format values
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# the below functions decoreted with @login_required are for redirect to login().
# not yet implemented!!
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # username = db.execute("SELECT username FROM users WHERE user_id= :user_id", user_id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE user_id=:user_id", user_id=session["user_id"])
    cash = cash[0]["cash"]
    user_stocks = db.execute("SELECT * FROM user_stock WHERE user_id=:user_id and shares > 0", user_id=session["user_id"])

    # create the list which is composed of user's information records
    users_info_list = []
    cash_stock_total = cash
    for item in user_stocks:
        stock_data = lookup(item["symbol"])
        total = item["shares"] * stock_data["price"]
        cash_stock_total += total
        user_tr = {"symbol": item["symbol"], "name": stock_data["name"],
                   "shares": item["shares"], "price": usd(stock_data["price"]), "total": usd(total)}
        users_info_list.append(user_tr)

    cash_stock_total = usd(cash_stock_total)
    cash = usd(cash)
    return render_template("index.html", users_info_list=users_info_list, cash=cash, cash_stock_total=cash_stock_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        stock_data = lookup(symbol)

        # if input symbol don't exists, return apology().
        if not stock_data:
            return apology(f"{symbol} don't exists!")

        user_cash = db.execute("SELECT cash FROM users WHERE user_id=:user_id", user_id=session["user_id"])
        pay_cash = stock_data["price"] * shares
        balance = user_cash[0]["cash"] - pay_cash
        if balance < 0:
            return apology("your cash is less than pay-cash !")

        # if all valid check is ok, insert record to transactions-table and user_stock-table
        db.execute("UPDATE users SET cash= :cash WHERE user_id=:user_id", cash=balance, user_id=session["user_id"])
        db.execute("INSERT INTO transactions(user_id, symbol, price, tr_shares) values(:user_id, :symbol, :price, :shares)",
                   user_id=session["user_id"], symbol=stock_data["symbol"], price=stock_data["price"], shares=shares)

        # insert user_stock or update user_stock
        own_shares = db.execute("SELECT shares FROM user_stock where user_id= :user_id and symbol= :symbol",
                                user_id=session["user_id"], symbol=stock_data["symbol"])

        if len(own_shares) == 0:
            db.execute("INSERT INTO user_stock(user_id, symbol, shares) values(:user_id, :symbol, :shares)",
                       user_id=session["user_id"], symbol=stock_data["symbol"], shares=shares)
        else:
            total_shares = own_shares[0]["shares"] + shares
            db.execute("UPDATE user_stock SET shares= :shares WHERE user_id=:user_id and symbol= :symbol",
                       shares=total_shares, user_id=session["user_id"], symbol=symbol)

        return redirect("/")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    # if input-username is in users-table, return False
    user_list = db.execute("SELECT username FROM users")
    username = request.args.get('username')
    print('check_user:', username)
    for user in user_list:
        print('user:', user["username"])
        if username == user["username"]:
            return jsonify(False)
    return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    hist_data = db.execute("SELECT * FROM transactions WHERE user_id=:user_id", user_id=session["user_id"])
    for item in hist_data:
        item["price"] = usd(item["price"])
    return render_template("history.html", hist_data=hist_data)


# login() and logout() are implemented completely.
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        symbol = request.form.get('symbol')
        stock_data = lookup(symbol)
        # print stock data
        if not stock_data:
            return apology(f"{symbol} don't exist!")
        else:
            return render_template("quoted.html", stock_data=stock_data)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template('register.html')

    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # if input username is already registerd, return apology().
        if username == "":
            return apology("Username is blank!", 400)
        if password == "":
            return apology("Password is blank!", 400)
        if confirmation == "":
            return apology("Confirmation is blank!", 400)

        users = db.execute("SELECT username FROM users")
        users = [dic["username"] for dic in users]
        if username in users:
            return apology("This Username is already registerd!", 400)
        else:
            # if password and confirmation don't match, return apology().
            if password != confirmation:
                return apology("Password and Password(again) don't match!", 400)
            # if all valid checks are ok, Insert users-table
            session["user_id"] = db.execute("INSERT into users (username, hash) values ( :username, :hash_value);",
                                            username=username, hash_value=generate_password_hash(password))
            # redirect to index.html
            return redirect('/')


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_stocks = db.execute("SELECT * FROM user_stock WHERE user_id=:user_id", user_id=session["user_id"])
        return render_template("sell.html", user_stocks=user_stocks)
    elif request.method == "POST":
        # get symbol and shares from template
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # calculate left_shares after buying stocks.
        own_shares = db.execute("SELECT shares FROM user_stock WHERE user_id=:user_id and symbol=:symbol",
                                user_id=session["user_id"], symbol=symbol)
        own_shares = own_shares[0]["shares"]
        left_shares = own_shares - shares

        # if left_shares is less than 1, return apology().
        if left_shares < 0:
            return apology(f"submitted shares are more than {symbol} shares you own!", 400)
        else:
            stock_data = lookup(symbol)
            user_cash = db.execute("SELECT cash FROM users WHERE user_id=:user_id", user_id=session["user_id"])
            get_cash = stock_data["price"] * shares
            balance = user_cash[0]["cash"] + get_cash

            # update all databases
            db.execute("UPDATE users SET cash= :cash WHERE user_id=:user_id", cash=balance, user_id=session["user_id"])
            db.execute("INSERT INTO transactions(user_id, symbol, price, tr_shares) values(:user_id, :symbol, :price, :shares)",
                       user_id=session["user_id"], symbol=symbol, price=stock_data["price"], shares=(-1) * shares)
            db.execute("UPDATE user_stock SET shares=:left_shares WHERE user_id=:user_id and symbol=:symbol",
                       left_shares=left_shares, user_id=session["user_id"], symbol=symbol)

            return redirect("/")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "GET":
        return render_template("add_cash.html")
    elif request.method == "POST":
        cash = int(request.form.get("cash"))
        own_cash = db.execute("SELECT cash FROM users WHERE user_id=:user_id", user_id=session["user_id"])
        own_cash = own_cash[0]["cash"]
        db.execute("UPDATE users SET cash=:new_cash WHERE user_id=:user_id", new_cash=cash+own_cash, user_id=session["user_id"])
        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
