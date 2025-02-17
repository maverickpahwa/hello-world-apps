# Version": 1.0.0

import csv
import os
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from faker import Faker

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins

CSV_FILE = "saved_data.csv"  # File to store data

# Ensure CSV file has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["createdTime", "fullname", "age", "mortality"])  # Column headers

fake = Faker()

@app.route("/api/")
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/api/heartbeat")
def heartbeat():
    return jsonify(status="running", service="flask-backend")

@app.route("/api/generate", methods=["GET"])
def generate_fake_data():
    """Generates fake people data (React will add `createdTime`)."""
    try:
        count = int(request.args.get("count", 1))  # Get count from query
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
def save_data():
    """Saves JSON data from React (including createdTime) to CSV."""
    data = request.json  # Get JSON from request

    if not isinstance(data, list):  # Ensure we receive a list of people
        return jsonify({"error": "Invalid JSON format"}), 400

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        for person in data:
            writer.writerow([person["createdTime"], person["fullname"], person["age"], person["mortality"]])

    return jsonify({"status": "success", "saved_count": len(data)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
