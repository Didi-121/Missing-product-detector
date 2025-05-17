import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("embeddings.db")
c = conn.cursor()

# Obtener nombres de todas las tablas
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = c.fetchall()

# Mostrar contenido de cada tabla
for tabla in tablas:
    nombre_tabla = tabla[0]
    print(f"\n📦 Tabla: {nombre_tabla}")

    # Obtener nombres de columnas
    c.execute(f"PRAGMA table_info({nombre_tabla});")
    columnas = [col[1] for col in c.fetchall()]
    print("🔑 Columnas:", columnas)

    # Obtener y mostrar filas
    c.execute(f"SELECT * FROM {nombre_tabla};")
    filas = c.fetchall()

    if filas:
        for fila in filas:
            print(f"➡️ {fila}")
    else:
        print("🕳️ Sin datos.")

conn.close()

