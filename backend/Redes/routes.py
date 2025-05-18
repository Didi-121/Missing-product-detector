# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=["POST"])
def add_detection():
    data = request.json
    label = data.get("nombre")
    confidence = data.get("edad")

    return 201

if __name__ == "__main__":
    app.run(debug=True)


