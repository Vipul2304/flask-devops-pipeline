from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    environment = os.getenv('ENVIRONMENT', 'development')
    version = os.getenv('APP_VERSION', 'v1.0.0')
    hostname = socket.gethostname()
    return f"""
    <h1>Welcome to My DevOps App 🚀</h1>
    <p>Environment: <strong>{environment}</strong></p>
    <p>Version: <strong>{version}</strong></p>
    <p>Container Hostname: <strong>{hostname}</strong></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
