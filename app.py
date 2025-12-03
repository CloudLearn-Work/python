from flask import Flask
import os

app = Flask(__name__)

# Example route
@app.route('/')
def home():
    return "Hello, Azure App Service!"

if __name__ == '__main__':
    app.run(debug=True)
