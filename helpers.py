from functools import wraps
from flask import session, redirect, g
import sqlite3

from datetime import datetime


# Configure to use SQLite database
DATABASE = "database.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(error):
    if hasattr(g, "db"):
        g.db.close()


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def calculate_financial_summary(username):
    # Get the current year
    current_year = datetime.now().year

    db = get_db()

    # Calculate total income
    total_income_query = "SELECT IFNULL(SUM(amount), 0.0) AS total FROM transactions WHERE type = 'income' AND username = ? AND strftime('%Y', date) = strftime('%Y', ? || '-01-01')"
    total_income_cursor = db.execute(total_income_query, (username, str(current_year)))
    total_income_result = total_income_cursor.fetchone()
    total_income = (
        total_income_result["total"]
        if total_income_result and total_income_result["total"] is not None
        else 0.0
    )


    # Calculate total expenses
    total_expenses_query = "SELECT IFNULL(SUM(amount), 0.0) AS total FROM transactions WHERE type = 'expense' AND username = ? AND strftime('%Y', date) = strftime('%Y', ? || '-01-01')"
    total_expenses_cursor = db.execute(total_expenses_query, (username, str(current_year)))
    total_expenses_result = total_expenses_cursor.fetchone()
    total_expenses = (
        total_expenses_result["total"]
        if total_expenses_result and total_expenses_result["total"] is not None
        else 0.0
    )

    # Calculate net profit
    net_profit = total_income - total_expenses

    return total_income, total_expenses, net_profit


def calculate_total_cost(parts_items, labour_items, other_items):
    total_cost = 0.0

    for items in [parts_items, labour_items, other_items]:
        for _, cost in items:
            total_cost += float(cost)

    return total_cost


def usd(value):
    """Format value as USD."""
    return f"{value:,.2f}"


def format_number_with_commas(value):
    return "{:,.2f}".format(float(value))


def format_number_with_commas_no_decimal(value):
    return "{:,.0f}".format(float(value))

def init_app(app):
    app.teardown_appcontext(close_db)
