import numpy as np
import sqlite3
import torch
import os
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Cargar modelo y processor de CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Ruta a carpeta con imágenes de prueba
image_path = input("foto: ")
image = Image.open(image_path)

# Obtener embedding de la imagen nueva
inputs = processor(images=image, return_tensors="pt")
new_embedding = model.get_image_features(**inputs)[0].detach().numpy()

# Ruta a la base de datos
db_path = os.path.join(os.path.dirname(os.getcwd()), "Data", "inv.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Recuperar todos los embeddings de la base de datos una sola vez
cursor.execute("SELECT id, vector FROM Productos")
db_embeddings = cursor.fetchall()

# Función para similitud coseno
def cosine_sim(a, b):
    if not isinstance(a, torch.Tensor):
        a = torch.tensor(a)
    if not isinstance(b, torch.Tensor):
        b = torch.tensor(b)
    return torch.nn.functional.cosine_similarity(a, b, dim=0).item()

    # Buscar el embedding más similar
best_product_id = None
best_score = -1

for product_id, vec_blob in db_embeddings:
    db_vector = np.frombuffer(vec_blob, dtype=np.float32)

    score = cosine_sim(new_embedding, db_vector)
    print("product ID: ",product_id, " ->",score)
    if score > best_score:
        best_score = score
        best_product_id = product_id

# Mostrar resultado
if best_product_id is not None:
    print(f"🔍 Más similar: product_id {best_product_id} (Similitud: {best_score*100:.2f}%)")

    # Consultar ubicación en la tabla Productos
    cursor.execute("""
        SELECT anaquel, charola, posicion
        FROM Productos
        WHERE id = ?
    """, (best_product_id,))
    ubicacion = cursor.fetchone()

    if ubicacion:
        anaquel, charola, posicion = ubicacion
        print(f"📍 Ubicación:\n - Anaquel: {anaquel}\n - Charola: {charola}\n - Posición: {posicion}")
    else:
        print("⚠️ No se encontró ubicación para este producto en la tabla Matrix.")
else:
    print("❌ No se encontró ningún embedding similar.")

conn.close()

