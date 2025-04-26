from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'smartstation@123'  # Secret key for flash messages

# Connect to the existing users.db database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash(f'Welcome back, {username}!')
            return redirect(url_for('dashboard'))  # Redirect to dashboard if login is successful
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))  # Redirect to login page if credentials are incorrect

    return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Insert the new user into the database
        conn = get_db_connection()
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

# Dashboard route (after login)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
