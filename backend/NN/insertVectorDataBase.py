import sqlite3
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os
import numpy as np

# Preparar modelo CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Conexión con base de datos
pathDB = os.path.join(os.path.dirname(os.getcwd()), "Data", "inv.db")
conn = sqlite3.connect(pathDB)
cursor = conn.cursor()

# Ruta a carpeta de imágenes
path = os.path.join(os.path.dirname(os.getcwd()), "Data/carasfrontales")
print("Ruta de imágenes:", path)

# Filtrar imágenes .png
images = [f for f in os.listdir(path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]


# Procesar cada imagen
for filename in images:
    # Extraer anaquel, charola, posicion, rotacion desde el nombre del archivo
    partes = os.path.splitext(filename)[0].split(",")
    anaquel, charola, posicion, rotacion = partes  # todos como texto (str)

    # Buscar product_id en tabla  
    print("AENTOSOST:",anaquel, charola, posicion)
    cursor.execute("""
    SELECT * FROM Productos
    WHERE anaquel = ? AND charola = ? AND posicion = ?
""", (anaquel, charola, posicion))

    result = cursor.fetchone()
    print("resultado",result)

    
    if result is None:
        print(f"⚠️ No se encontró product_id para: {filename}")
        continue

    product_id = result[0]

    # Cargar imagen y generar embedding
    img = Image.open(os.path.join(path, filename)).convert("RGB")
    inputs = processor(images=img, return_tensors="pt")
    embedding = model.get_image_features(**inputs)[0].detach().numpy()
    vector_blob = embedding.astype(np.float32).tobytes()

    # Insertar en tabla Embeddings
    cursor.execute("""
        INSERT INTO Productos (name, codigoBarras, vector, created,anaquel, charola, posicion, rotacion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (result[1], result[2], vector_blob, result[4],result[5], result[6], result[7], rotacion))
    print(f"✅ Procesado: {filename} → producto {product_id}, rotación: {rotacion}")



cursor.execute("""
DELETE FROM Productos
WHERE vector IS NULL
""")

# Guardar y cerrar
conn.commit()
conn.close()
print("✅ Todos los embeddings fueron guardados.")

