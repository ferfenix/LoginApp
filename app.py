# Imports
from flask import Flask, render_template, request, redirect
import sqlite3
# Setup
app = Flask(__name__)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        connectiondb = sqlite3.connect('usersdata.db')
        cursor = connectiondb.cursor()
        username = request.form['username']
        password = request.form['password']
        query = "SELECT name,password FROM users where name = '"+username+"' and password = '"+password+"'"
        cursor.execute(query)
        results = cursor.fetchall()
# Validation
        if len(results) == 0:
            print("El usuario y/o contraseña no son correctos, registrese")
            return render_template("not_access.html")
        else:
            return render_template("logged_in.html")
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def registerpage():
    if request.method == "POST":
        connectiondb = sqlite3.connect('usersdata.db')
        cursor = connectiondb.cursor()
        username = request.form['username']
        password = request.form['password']
        query2 = "INSERT INTO users VALUES ('{}','{}')".format(username, password)
        cursor.execute(query2)
        connectiondb.commit()
        return render_template("user_registered.html")
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)