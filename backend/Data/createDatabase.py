import sqlite3

# Ruta a la base de datos
db_path = "inv.db"

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear tabla ProductoCompleto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    codigoBarras TEXT,
    vector BLOB,
    created TEXT DEFAULT CURRENT_TIMESTAMP,
    anaquel TEXT NOT NULL,
    charola TEXT NOT NULL,
    posicion TEXT NOT NULL
);
""")

# Guardar y cerrar
conn.commit()
conn.close()

print("Tabla 'ProductoCompleto' creada exitosamente en la base de datos.")

