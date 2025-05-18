import sqlite3
import pandas as pd
import os

# Ruta del CSV y base de datos
csv_path = "datos.csv"
db_path = "inv.db"

# Cargar datos del CSV
df = pd.read_csv(csv_path)

# Conectar a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insertar datos del CSV
for _, row in df.iterrows():
    name = str(row["Nombre"]).strip()
    barcode = str(int(float(row["CB"]))) if not pd.isna(row["CB"]) else None
    anaquel = int(row["Anaquel"])
    hilera = int(row["Charola"])
    posicion = int(row["Posicion"])

    if name and barcode:
        try:
            cursor.execute(
                "INSERT INTO Productos(name, codigoBarras, anaquel, charola, posicion) VALUES (?, ?, ?, ?, ?)",
                (name, barcode, anaquel, hilera, posicion)
            )
        except Exception as e:
            print(f"Error al insertar el producto '{name}': {e}")

# Guardar y cerrar
conn.commit()
conn.close()

print("Importación completada correctamente.")

