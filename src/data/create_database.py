import sqlite3

# Create (or open) the database
conn = sqlite3.connect("company.db")

cursor = conn.cursor()

# Create the employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    department TEXT,
    city TEXT,
    salary REAL
)
""")

# Insert sample data
employees = [
    (1, "IT", "Paris", 4500),
    (2, "Sales", "London", 3500),
    (3, "HR", "Berlin", 3200),
    (4, "Marketing", "Madrid", 4000),
    (5, "Finance", "Rome", 5000),
    (6, "Support", "Lisbon", 3000)
]

cursor.executemany("""
INSERT OR REPLACE INTO employees
VALUES (?, ?, ?, ?)
""", employees)

conn.commit()
conn.close()

print("✅ company.db created successfully!")