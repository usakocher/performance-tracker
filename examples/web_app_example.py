"""
Web application performance monitoring example

This demonstrates how to use PyPerformance in a Flask web application
to monitor API endpoint performance.
"""

try:
    from flask import Flask, jsonify
except ImportError:
    print("Flask not installed. Install with: pip install flask")
    exit(1)

import random
import time

from pyperformance import get_performance_stats as get_stats
from pyperformance import performance_monitor, show_performance_report

app = Flask(__name__)

# Database simulation
fake_users = [
    {"id": i, "name": f"User {i}", "email": f"user{i}@example.com"}
    for i in range(1, 1001)
]


@performance_monitor(track_memory=True)
def fetch_user_from_db(user_id):
    """Simulate database query with variable latency"""
    # Simulate database query time
    time.sleep(random.uniform(0.01, 0.05))

    for user in fake_users:
        if user["id"] == user_id:
            return user
    return None


@performance_monitor()
def process_user_data(user):
    """Simulate data processing"""
    time.sleep(random.uniform(0.005, 0.015))

    processed = user.copy()
    processed["processed_at"] = time.time()
    processed["status"] = "active"
    return processed


@performance_monitor(track_memory=True)
def generate_report_data():
    """Simulate expensive report generation"""
    time.sleep(0.1)  # Simulate complex calculations

    report = {
        "total_users": len(fake_users),
        "active_users": random.randint(800, 950),
        "generated_at": time.time(),
    }
    return report


# API Endpoints
@app.route("/users/<int:user_id>")
def get_user(user_id):
    """Get user by ID"""
    user = fetch_user_from_db(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    processed_user = process_user_data(user)
    return jsonify(processed_user)


@app.route("/report")
def get_report():
    """Generate and return system report"""
    report = generate_report_data()
    return jsonify(report)


@app.route("/performance")
def get_performance_stats():
    """Get current performance statistics"""
    stats = get_stats()
    return jsonify(stats)


@app.route("/performance/report")
def performance_report():
    """Get formatted performance report"""
    import io
    import sys

    # Capture the report output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    show_performance_report()

    sys.stdout = old_stdout
    report_text = buffer.getvalue()

    return f"<pre>{report_text}</pre>"


if __name__ == "__main__":
    print("Starting Flask app with PyPerformance monitoring...")
    print("Visit these endpoints:")
    print("  http://localhost:5000/users/1")
    print("  http://localhost:5000/report")
    print("  http://localhost:5000/performance")
    print("  http://localhost:5000/performance/report")

    app.run(debug=True, port=5000)
