from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for development

@app.route('/')
def home():
    return render_template('index.html')  # Render frontend HTML from /templates

@app.route('/crypto/<coin_name>', methods=['GET'])
def get_crypto_data(coin_name):
    try:
        conn = sqlite3.connect('crypto_data.db')
        conn.row_factory = sqlite3.Row  # Return dict-like rows
        cursor = conn.cursor()

        # Query the selected coin's table
        query = f"SELECT * FROM '{coin_name}' ORDER BY Date DESC"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        # Convert each row to a dictionary
        result = [dict(row) for row in rows]
        return jsonify(result), 200

    except sqlite3.OperationalError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)