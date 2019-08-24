from flask import flask, render_template, redirect
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/asset')
def asset():
    return render_template('asset.html')


@app.route('/asset/edit')
def assetEdit():
    return render_template('assetEdit.html')


@app.route('/board')
def board():
    return render_template('board.html')


if __name__ == "__main__":
    app.run(debug=True)
