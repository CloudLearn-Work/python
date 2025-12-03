# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# A simple route
@app.route('/')
def home():
    return "Hello, Azure!"

# A sample API endpoint
@app.route('/api/data')
def data():
    return jsonify({"message": "This is an API response"})

# Static file route
@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True)  # Don't run this line on production, it’s only for development.


