import csv
import os
import random
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from faker import Faker

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize Flask-Limiter (Throttle Requests)
limiter = Limiter(get_remote_address, app=app, default_limits=["60 per minute"])  # Global limit

# Define CSV file location inside the mounted volume
CSV_DIR = "/app/data"
CSV_FILE = os.path.join(CSV_DIR, "saved_data.csv")

# Ensure CSV directory exists
os.makedirs(CSV_DIR, exist_ok=True)

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["createdTime", "fullname", "age", "mortality"])  # Column headers

fake = Faker()

@app.route("/api/")
@limiter.limit("10 per minute")  # Limit homepage API to 10 requests per minute
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/api/heartbeat")
@limiter.limit("20 per minute")  # Allow 20 checks per minute
def heartbeat():
    return jsonify(status="running", service="flask-backend")

@app.route("/api/generate", methods=["GET"])
@limiter.limit("5 per minute")  # Limit to 5 requests per minute
def generate_fake_data():
    """Generates fake people data (React will add `createdTime`)."""
    try:
        count = int(request.args.get("count", 1))
        count = min(max(count, 1), 20)  # Ensure count is between 1 and 20

        fake_data = [
            {
                "fullname": fake.name(),
                "age": random.randint(18, 99),
                "mortality": random.choice([0, 1])
            }
            for _ in range(count)
        ]
        return jsonify(fake_data)
    
    except ValueError:
        return jsonify(error="Invalid count"), 400

@app.route("/api/save", methods=["POST"])
@limiter.limit("3 per minute")  # Limit saving data to 3 times per minute
def save_data():
    """Saves JSON data from React (including createdTime) to CSV."""
    data = request.json

    if not isinstance(data, list):
        return jsonify({"error": "Invalid JSON format"}), 400

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        for person in data:
            writer.writerow([person["createdTime"], person["fullname"], person["age"], person["mortality"]])

    return jsonify({"status": "success", "saved_count": len(data)})

@app.route("/api/records", methods=["GET"])
#@limiter.limit("5 per minute")  # Limit to 5 record retrievals per minute
def get_records():
    """Loads CSV and paginates 10 records per page."""
    page = int(request.args.get("page", 1))
    records_per_page = 10

    try:
        with open(CSV_FILE, mode="r") as file:
            reader = list(csv.reader(file))
            if len(reader) <= 1:
                return jsonify({"data": [], "total_pages": 0, "current_page": page})

            headers = reader[0]
            data = [dict(zip(headers, row)) for row in reader[1:]]

        total_records = len(data)
        total_pages = (total_records + records_per_page - 1) // records_per_page

        start = (page - 1) * records_per_page
        end = start + records_per_page

        return jsonify({
            "data": data[start:end],
            "total_pages": total_pages,
            "current_page": page
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
