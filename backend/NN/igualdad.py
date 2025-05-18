import numpy as np
import sqlite3
import torch
from PIL import Image, ImageTk
import os
from transformers import CLIPProcessor, CLIPModel
import tkinter as tk


# Cargar modelo y processor de CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Cargar imagen a comparar
path = os.path.join(os.path.dirname(os.getcwd()), "NN/test2")

print("Ruta de imágenes:", path)
images = [f for f in os.listdir(path) if f.lower().endswith((".png"))]

anss = []

sum = 0
for i in images:
    print(i)
    img_new = Image.open(path +"/"+ i)
    inputs_new = processor(images=img_new, return_tensors="pt")
    embedding_new = model.get_image_features(**inputs_new)[0].detach().numpy()
    
    # Conectar a la base de datos y obtener embeddings guardados
    db_path = os.path.join(os.path.dirname(os.getcwd()), "Data", "inventario.db")
    conn = sqlite3.connect(db_path)

    c = conn.cursor()
    c.execute("SELECT label, vector FROM embeddings")
    results = c.fetchall()
    conn.close()

    # Función para similitud coseno
    def cosine_sim(a, b):
        if not isinstance(a, torch.Tensor):
            a = torch.tensor(a)
        if not isinstance(b, torch.Tensor):
            b = torch.tensor(b)
        return torch.nn.functional.cosine_similarity(a, b, dim=0).item()


    # Comparar con cada embedding en la base de datos
    best_label = None
    best_score = -1

    for label, vec_blob in results:
        vec = np.frombuffer(vec_blob, dtype=np.float32)
        score = cosine_sim(embedding_new, vec)
        if score > best_score:
            best_score = score
            best_label = label

    print(f"Categoría más similar: {best_label} ({best_score*100:.2f}%)")
    print("Label: " + i)
    print("Label comparado: " + best_label)


    #pedir input de verificacion, 0 ,1,2 (nqada, similar, igual)
    ans = input("similitud (0,1,2) ")
    if (ans == 2):
        sum += 1
    #guardar en una lista
    anss.append(ans)

print(ans)
print(sum/len(images)-7)
