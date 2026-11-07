from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Application Reliability Monitor is running!",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)