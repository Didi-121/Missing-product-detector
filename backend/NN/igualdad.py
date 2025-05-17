import numpy as np
import sqlite3
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Cargar modelo y processor de CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Cargar imagen a comparar
path = os.path.join(os.path.dirname(os.getcwd()), "Data/testing")
print("Ruta de imágenes:", path)
images = [f for f in os.listdir(path) if f.lower().endswith((".png"))]

for i in images:
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
