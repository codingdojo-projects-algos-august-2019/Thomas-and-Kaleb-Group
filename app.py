from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "beat_navy"
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/loginregister")
def login_register_main():
    return render_template("login.html")


@app.route("/register", methods=["POST"])
def register_user():
    is_valid = True
    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("First Name must be at least 2 characters long")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last Name must be at least 2 characters long")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("Password must be at least 8 characters long")
    if request.form['c_password'] != request.form['password']:
        is_valid = False
        flash("Passwords do not match")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please use valid email")

    if is_valid:  # passes all validations and moves user to next screen
        # Create a connection to the db
        mysql = connectToMySQL('assets')
        # Build my query
        query = "INSERT into users (fname, lname, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, %(pass)s, NOW(), NOW());"
        # Pass Relevant Data
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'email': request.form['email'],
            'pass': bcrypt.generate_password_hash(request.form['password'])
        }
        # Commit to  query
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id

        return redirect("/asset")
    else:  # does not pass validations and shows users the errors
        return redirect("/loginregister")

    return redirect("/loginregister")


@app.route("/login", methods=["POST"])
def login_user():
    # 2. Create a route that the form form step one will post to and then validate, check with db
    is_valid = True
    if len(request.form['email']) < 2:
        is_valid = False
        flash("Please use a valid email")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("Password enter your password")

    if not is_valid:  # users goes back to put in relevant data and shows users the errors
        return redirect("/")
    else:  # does pass validations and checks the data base
        # Create a connection to the db
        mysql = connectToMySQL('assets')
        # Build my query to see if the email exists
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        data = {
            'email': request.form['email']
        }
        user = mysql.query_db(query, data)
        if user:
            hashed_password = user[0]['password']
            if bcrypt.check_password_hash(hashed_password, request.form['password']):
                session['user_id'] = user[0]['id']
                return redirect("/asset")
            else:
                flash("Password invalid")
                return redirect("/loginregister")

        else:
            flash("Please use a valid email address")
            return redirect("/loginregister")
        return redirect("/loginregister")

    return redirect("/loginregister")


@app.route("/logout")
def logout_user():
    session.clear()
    return redirect("/")


@app.route('/asset')
def asset():
    if 'user_id' not in session:
        return redirect("/")

    mysql = connectToMySQL('assets')
    query = "SELECT * FROM users WHERE users.id = %(id)s"
    data = {
        'id': session['user_id']
    }
    user = mysql.query_db(query, data)

    mysql = connectToMySQL('assets')
    query = "SELECT * FROM assets WHERE assets.user_id = %(id)s"
    data = {
        'id': session['user_id']
    }
    asset = mysql.query_db(query, data)

    mysql = connectToMySQL('assets')
    query = "SELECT count(idasset) as assets, sum(value) as total_value FROM assets WHERE assets.user_id = %(id)s"
    data = {
        'id': session['user_id']
    }
    asset_values = mysql.query_db(query, data)

    return render_template("asset.html", user=user[0], asset=asset, asset_values=asset_values[0])


@app.route("/post_asset", methods=["POST"])
def post_asset():

    # Build Validattions for Inputs
    #is_valid = True
    # if len(request.form['location']) < 3:
    #    is_valid = False
    #    flash('Thought must be at least 3 characters')
    # if len(request.form['location']) >= 46:
    #    is_valid = False
    #    flash('Thought cannot be more than 45 characters')

    mysql = connectToMySQL('assets')
    query = "INSERT into assets (user_id, description, count, brand, make, year, value, location, comments, created_at, updated_at) VALUES (%(uid)s, %(des)s, %(ct)s, %(bd)s, %(mk)s, %(yr)s, %(val)s, %(loc)s, %(cmt)s, NOW(), NOW());"
    data = {
        'uid': session['user_id'],
        'des': request.form['description'],
        'ct': request.form['count'],
        'bd': request.form['brand'],
        'mk': request.form['make'],
        'yr': request.form['year'],
        'val': request.form['value'],
        'loc': request.form['location'],
        'cmt': request.form['comments']
    }
    asset_id = mysql.query_db(query, data)
    print(asset_id)

    return redirect("/asset")


@app.route("/edit/<m_id>")
def edit_asset(m_id):

    mysql = connectToMySQL('assets')
    query = "SELECT * FROM users WHERE users.id = %(id)s"
    data = {
        'id': session['user_id']
    }
    user = mysql.query_db(query, data)

    mysql = connectToMySQL('assets')
    query = "SELECT * FROM assets WHERE idasset = %(mid)s"
    data = {
        'mid': m_id
    }
    asset = mysql.query_db(query, data)

    return render_template("assetEdit.html", user=user[0], asset=asset)


@app.route("/deleteasset/<m_id>")
def delete_asset(m_id):

    mysql = connectToMySQL('assets')
    query = "DELETE FROM assets WHERE idasset = %(mid)s;"
    data = {
        'mid': m_id
    }
    mysql.query_db(query, data)

    return redirect("/asset")


@app.route('/board')
def board():
    return render_template('board.html')


if __name__ == "__main__":
    app.run(debug=True)
