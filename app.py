import os
import sys
from datetime import date
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql


from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date


app = Flask(__name__, template_folder='templates')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def template_test():
    return render_template('/start.html')

@app.route("/sznio", methods=["GET", "POST"])
def temp():
    return render_template('/start.html')