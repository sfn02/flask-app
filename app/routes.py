from flask import render_template_string, request, redirect, session, url_for
from app import app

# Dummy user store
users = {}

@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome, {session['user']}!"
    return "You are not logged in. <a href='/login'>Login</a>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

