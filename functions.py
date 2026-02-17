import sqlite3

def get_data():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def delete_table():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS my_table')
    conn.commit()
    conn.close()

def create_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            link TEXT,
            image TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data_db(title, price, link, image):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO my_table (title, price, link, image) VALUES (?, ?, ?, ?)
    ''', (title, price, link, image))
    conn.commit()
    conn.close()    

# delete_table()
# create_db()
