import sqlite3

# Create a new database or connect to an existing one
conn = sqlite3.connect('users.db')

# Create a table for users if it doesn't already exist
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

# Create a table for inventory items (stationary)
conn.execute('''
CREATE TABLE IF NOT EXISTS stationary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Save changes and close connection
conn.commit()
conn.close()

print("✅ Database and tables created successfully.")
