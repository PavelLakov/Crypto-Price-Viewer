from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "crypto_data.db")


@app.route("/")
def home():
    return render_template("index.html")


def normalize_table_name(coin_name: str) -> str:
    # Frontend sends "Bitcoin", DB tables are "bitcoin"
    return coin_name.strip().replace(" ", "_").lower()


def date_to_iso_expr():
    # Date stored as "MM/DD/YYYY" -> convert to "YYYY-MM-DD" for proper ordering/filtering
    return "substr(Date, 7, 4) || '-' || substr(Date, 1, 2) || '-' || substr(Date, 4, 2)"


@app.route("/crypto/<coin_name>", methods=["GET"])
def get_crypto_data(coin_name):
    table = normalize_table_name(coin_name)

    start = request.args.get("start")  # expecting YYYY-MM-DD
    end = request.args.get("end")      # expecting YYYY-MM-DD

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        iso_date = date_to_iso_expr()

        sql = f"SELECT * FROM {table}"
        params = []

        # optional date filter (ISO compare)
        if start and end:
            sql += f" WHERE {iso_date} BETWEEN ? AND ?"
            params.extend([start, end])
        elif start:
            sql += f" WHERE {iso_date} >= ?"
            params.append(start)
        elif end:
            sql += f" WHERE {iso_date} <= ?"
            params.append(end)

        sql += f" ORDER BY {iso_date} DESC"

        cur.execute(sql, params)
        rows = cur.fetchall()
        conn.close()

        return jsonify([dict(r) for r in rows]), 200

    except sqlite3.OperationalError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
