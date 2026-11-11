import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'status_log.db')

print(f"Database path: {db_path}")
print(f"File exists: {os.path.exists(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check table structure
cursor.execute("PRAGMA table_info(status_log)")
columns = cursor.fetchall()
print(f"\nTable columns: {columns}")

# Count all entries
cursor.execute("SELECT COUNT(*) FROM status_log")
total = cursor.fetchone()[0]
print(f"\nTotal entries in database: {total}")

# Show ALL entries
cursor.execute("SELECT * FROM status_log ORDER BY id DESC")
rows = cursor.fetchall()

print(f"\nShowing all {len(rows)} entries:")
for i, row in enumerate(rows, 1):
    print(f"{i}. {row}")

conn.close()