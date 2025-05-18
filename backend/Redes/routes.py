# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=["POST"])
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


