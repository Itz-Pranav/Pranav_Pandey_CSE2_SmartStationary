import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.secret_key = 'smartstation@123'  # you can change this if you want


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash(f'Welcome back, {username}!')
            return redirect(url_for('dashboard'))  # You can later change this to go to a dashboard
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           (username, password, role))
            conn.commit()
            flash('✅ Registration successful! You can now login.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('⚠️ Username already exists. Try a different one.')
            return redirect(url_for('register'))
        finally:
            conn.close()
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
