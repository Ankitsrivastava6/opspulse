from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "opspulse_requests_total",
    "Total number of requests received by OpsPulse"
)


@app.before_request
def count_request():
    REQUEST_COUNT.inc()


@app.get("/")
def home():
    return jsonify(
        application="OpsPulse",
        version="1.0.0",
        message="OpsPulse DevOps project is running"
    )


@app.get("/health")
def health():
    return jsonify(
        status="healthy"
    )


@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
