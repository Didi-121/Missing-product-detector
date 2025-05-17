import sqlite3
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
print("flag1")
# Preparar modelo
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Imagen base
img = Image.open("test1.png")
inputs = processor(images=img, return_tensors="pt")
embedding = model.get_image_features(**inputs)[0]  # [512] vector

# Conexión con base de datos
conn = sqlite3.connect("embeddings.db")
c = conn.cursor()

# Crear tabla
c.execute('''
CREATE TABLE IF NOT EXISTS embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT,
    vector BLOB
)
''')

# Guardar embedding
c.execute("INSERT INTO embeddings (label, vector) VALUES (?, ?)",
          ("cat", embedding.detach().numpy().tobytes()))
conn.commit()
conn.close()

