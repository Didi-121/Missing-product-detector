from flask import Flask, request, jsonify
from flask_cors import CORS
from image_info import image_info
from PIL import Image
import base64
import io

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=["POST"])
def add_detection():
    data = request.json
    image_b64 = data.get("imagen")  # ← Ya es string base64, no usar .bytes()
    posicion = data.get("posicion")  # ej. "3,2,1"
    
    # Decodificar base64 → bytes
    image_bytes = base64.b64decode(image_b64)
    
    # Cargar imagen desde memoria
    image = Image.open(io.BytesIO(image_bytes))
    
    # Guardar con nombre según la posición
    image.save("temp.png")

    # Obtener información y responder
    response = image_info(posicion)

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)