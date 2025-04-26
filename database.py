import sqlite3

# Create a new database or connect to existing one
conn = sqlite3.connect('users.db')

# Create a table for users
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

# Save changes and close connection
conn.commit()
conn.close()

print("✅ Database and table created successfully.")
