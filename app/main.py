from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, jsonify, Response
from datetime import datetime
from prometheus_client import Counter, Gauge, Histogram


app = Flask(__name__)
health_checks_total = Counter(
    "app_health_checks_total",
    "Total number of application health checks"
)
app_health_status = Gauge(
    "app_health_status",
    "Application health status (1=healthy, 0=unhealthy)"
)
health_check_duration = Histogram(
    "app_health_check_duration_seconds",
    "Time spent processing health check requests"
)
@app.route("/")
def home():
    return jsonify({
        "message": "Application Reliability Monitor is running!",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/health")
def health():
    with health_check_duration.time():
        health_checks_total.inc()
        app_health_status.set(1)

        return jsonify({
            "status": "healthy",
            "timestamp": datetime.now().isoformat()
        }), 200

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)