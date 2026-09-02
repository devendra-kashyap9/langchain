import sqlite3

conn = sqlite3.connect('SalesDB/sales.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,              
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)''')

cursor.execute('''
INSERT INTO sales (product_name, quantity, price, sale_date) VALUES
    ('Product A', 10, 19.99, '2023-01-01'),
    ('Product B', 5, 29.99, '2023-01-02'),
    ('Product C', 2, 39.99, '2023-01-03')
''')

conn.commit()
conn.close()