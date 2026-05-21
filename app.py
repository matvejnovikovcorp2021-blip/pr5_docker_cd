from flask import Flask, Response
from prometheus_client import Counter, generate_latest, REGISTRY
import time

app = Flask(__name__)

# Метрики
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_TIME = Counter('http_request_duration_seconds', 'Request duration in seconds')

@app.route('/')
def home():
    start = time.time()
    REQUEST_COUNT.inc()
    result = 'Hello, Continuous Deployment with Monitoring!'
    REQUEST_TIME.inc(time.time() - start)
    return result

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)