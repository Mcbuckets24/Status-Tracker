import sqlite3
import subprocess
import os
from datetime import datetime


def add_status(status_text):
    # Add to database
    db_path = os.path.join(os.path.dirname(__file__), 'status_log.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO status_log (status, timestamp) VALUES (?, ?)",
                   (status_text, timestamp))
    conn.commit()
    conn.close()

    print(f"Status added: {status_text}")

    # Git commands
    subprocess.run(['git', 'add', 'status_log.db'])
    subprocess.run(['git', 'commit', '-m', f'Add status: {status_text[:50]}'])
    subprocess.run(['git', 'push'])

    print("Pushed to GitHub! GitHub Actions will update the JSON.")


# Usage
if __name__ == '__main__':
    status = input("Enter your status: ")
    add_status(status)