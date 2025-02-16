from flask import Flask, request, jsonify
from flask_cors import CORS
from faker import Faker
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

fake = Faker()

@app.route("/")
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/heartbeat")
def heartbeat():
    return jsonify(status="running", service="flask-backend")

@app.route("/generate", methods=["GET"])
def generate_fake_data():
    try:
        count = int(request.args.get("count", 1))  # Get value from slider (default: 1)
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
