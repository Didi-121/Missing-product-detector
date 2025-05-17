# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase_utils import insert_detection, receive_data

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "API con Flask + SDK de Supabase funcionando!"

@app.route("/info", methods=["GET"])
def data():
    response = receive_data()
    return jsonify(response.data), 201


@app.route("/detections", methods=["POST"])
def add_detection():
    data = request.json
    label = data.get("label")
    confidence = data.get("confidence")
    timestamp = data.get("timestamp")


    response = insert_detection(label, confidence, timestamp)

    # 🛡️ Validación de que response existe
    if response and response.data:
        return jsonify({"message": "Detección guardada correctamente"}), 201

    elif response and response.error:
        return jsonify({"error": str(response.error)}), 400
    else:
        # Error grave: no hubo ni response ni error claro
        return jsonify({"error": "Internal error or no response from Supabase"}), 500

if __name__ == "__main__":
    app.run(debug=True)


