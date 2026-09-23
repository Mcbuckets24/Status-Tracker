from flask import Flask, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Path to your .db file
db_path = os.path.join(os.path.dirname(__file__), 'status_log.db')

@app.route('/api/statuses')
def get_statuses():
    """Get all statuses from the database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Fetch all statuses and timestamps, ordered by newest first
        cursor.execute("SELECT status, timestamp FROM status_log ORDER BY id DESC")
        statuses = [{"status": row[0], "timestamp": row[1]} for row in cursor.fetchall()]
        
        conn.close()
        return jsonify(statuses)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/statuses/latest')
def get_latest_status():
    """Get the most recent status"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT status, timestamp FROM status_log ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return jsonify({"status": result[0], "timestamp": result[1]})
        else:
            return jsonify({"error": "No statuses found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting status API server...")
    print("API endpoints:")
    print("  GET /api/statuses - Get all statuses")
    print("  GET /api/statuses/latest - Get latest status")
    print("Access your status page at: http://localhost:5000/status.html")
    app.run(debug=True, host='0.0.0.0', port=5000)
