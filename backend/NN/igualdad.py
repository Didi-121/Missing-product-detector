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
path = os.path.join(os.path.dirname(os.getcwd()), "Data/testing")
print("Ruta de imágenes:", path)
images = [f for f in os.listdir(path) if f.lower().endswith((".png"))]

anss = []

for i in images:
    ventana = tk.Tk()
    ventana.title("cine")

    img_new = Image.open(i)
    inputs_new = processor(images=img_new, return_tensors="pt")
    embedding_new = model.get_image_features(**inputs_new)[0].detach().numpy()
    
    # Conectar a la base de datos y obtener embeddings guardados
    conn = sqlite3.connect("embeddings.db")
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

    #mostrar la imagen y el porcentaje
    imagen1_tk = ImageTk.PhotoImage(img_new)
    imagen2_tk = ImageTk.PhotoImage(Image.open(os.path.join(path, best_label + ".png")))

    label1 = tk.Label(ventana, image=imagen1_tk)
    label1.pack(side="left")
    label2 = tk.Label(ventana, image=imagen2_tk)
    label2.pack(side="right")

    #pedir input de verificacion, 0 ,1,2 (nqada, similar, igual)
    ans = input("similitud (0,1,2) ")
    #cerrar ventana
    ventana.destroy()
    #guardar en una lista
    anss = anss.append(ans)