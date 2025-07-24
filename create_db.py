import sqlite3

# Connect to SQLite database (will create if it doesn't exist)
conn = sqlite3.connect('contracts.db')
cursor = conn.cursor()

# Create contracts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_name TEXT NOT NULL,
    supplier_name TEXT NOT NULL,
    contract_number TEXT UNIQUE NOT NULL,
    start_date TEXT,
    end_date TEXT
)
''')

# Insert sample contract
cursor.execute('''
INSERT OR IGNORE INTO contracts (contract_name, supplier_name, contract_number, start_date, end_date)
VALUES (?, ?, ?, ?, ?)
''', ('IT Services Agreement', 'Acme Corp', 'ACME-001', '2024-01-01', '2026-01-01'))

conn.commit()
conn.close()

print("Database created and sample contract inserted.")