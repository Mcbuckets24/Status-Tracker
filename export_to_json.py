import sqlite3
import json
import os

# Path to your .db file
db_path = os.path.join(os.path.dirname(__file__), 'status_log.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all statuses and timestamps
cursor.execute("SELECT status, timestamp FROM status_log ORDER BY id DESC")
statuses = [{"status": row[0], "timestamp": row[1]} for row in cursor.fetchall()]

conn.close()

# Save to a JSON file
json_path = os.path.join(os.path.dirname(__file__), 'statuses.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(statuses, f, ensure_ascii=False, indent=2)

print(f"Exported {len(statuses)} statuses to {json_path}")


