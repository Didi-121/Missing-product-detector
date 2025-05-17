import numpy as np
import sqlite3
import torch
from PIL import Image

# Nueva imagen
img_new = Image.open("unknown.jpg")
inputs_new = processor(images=img_new, return_tensors="pt")
embedding_new = model.get_image_features(**inputs_new)[0]

# Obtener todos los vectores de la base
conn = sqlite3.connect("embeddings.db")
c = conn.cursor()
c.execute("SELECT label, vector FROM embeddings")
results = c.fetchall()
conn.close()

# Comparar usando similitud coseno
def cosine_sim(a, b):
    a = torch.tensor(a)
    b = torch.tensor(b)
    return torch.nn.functional.cosine_similarity(a, b, dim=0).item()

best_label = None
best_score = -1

for label, vec_blob in results:
    vec = np.frombuffer(vec_blob, dtype=np.float32)
    score = cosine_sim(embedding_new, vec)
    if score > best_score:
        best_score = score
        best_label = label

print(f"Categoría más similar: {best_label} ({best_score*100:.2f}%)")

