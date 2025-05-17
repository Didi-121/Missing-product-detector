import sqlite3
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os

# Preparar modelo
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Conexión con base de datos
conn = sqlite3.connect("embeddings.db")
c = conn.cursor()

images = [f for f in os.listdir(r"backend/Data/chopped_products") if f.lower().endswith((".png"))]

# Imagen base
for i in images:
    img = Image.open(i)
    inputs = processor(images=img, return_tensors="pt")
    embedding = model.get_image_features(**inputs)[0]  # [512] vector
    
    # Guardar embedding
    c.execute("INSERT INTO embeddings (label, vector) VALUES (?, ?)",
            (os.path.splitext(os.path.basename(i))[0]
    , embedding.detach().numpy().tobytes()))

    conn.commit()
    conn.close()

