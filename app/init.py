from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({
        "app": "Ferromaderas",
        "version": "1.0.0",
        "status": "running",
        "message": "Welcome to Ferromaderas User Management API"
    })


@app.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "app": "Ferromaderas"
    })


if __name__ == "__main__":
    app.run(debug=True)