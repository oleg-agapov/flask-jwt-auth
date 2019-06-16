from flask import jsonify

from run import app


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})
