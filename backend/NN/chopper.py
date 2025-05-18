import cv2
import os
import matplotlib.pyplot as plt

def chop_image(imagen_path, output_dir='output', grid_output='imagen_con_cuadros.png', shelf=0):

    vec2 = [
    [[218, 350, 490, 720], [243]],
    [[180, 318, 463, 720], [451]],
    [[96, 152, 264, 373, 446, 519, 590, 720], [682]],
    [[120, 188, 252, 308, 368, 485, 720], [960]]
    ]

    vec1 = [
        [[126, 185, 236, 309, 375, 439, 720], [223]],
        [[111, 190, 243, 321, 510, 720], [448]],
        [[110, 185, 249, 317, 366, 428, 535, 720], [726]],
        [[152, 270, 380, 500, 621, 720], [960]]
    ]

    vec = vec1 if shelf == 0 else vec2

    img = cv2.imread(imagen_path)
    
    alto_img = img.shape[0]
    os.makedirs(output_dir, exist_ok=True)
    
    # Obtener líneas Y invertidas para OpenCV
    y_lines = [v[1][0] for v in vec]
    y_lines = [0] + y_lines
    y_coords = [alto_img - y for y in y_lines]

    # Dibujar todos los rectángulos para referencia
    for i, (x_list, _) in enumerate(vec):
        y_top = y_coords[i+1]
        y_bottom = y_coords[i]
        
        # Invertir x_list para recorrer de derecha a izquierda
        x_list_inv = x_list[::-1]
        
        for j, x_end in enumerate(x_list_inv):
            x_start = 0 if j == 0 else x_list_inv[j-1]
            left = min(x_start, x_end)
            right = max(x_start, x_end)
            top = min(y_top, y_bottom)
            bottom = max(y_top, y_bottom)
            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)

    #cv2.imwrite(grid_output, img)

    # Ahora cortamos y guardamos las imágenes en orden derecha-izquierda, abajo-arriba
    recortes = []
    for i in reversed(range(len(vec))):  # de abajo a arriba (invertir filas)
        x_list, _ = vec[i]
        y_top = y_coords[i+1]
        y_bottom = y_coords[i]
        
        # recorrer x de derecha a izquierda
        for j in reversed(range(len(x_list))):
            x_end = x_list[j]
            x_start = 0 if j == 0 else x_list[j-1]

            left = min(x_start, x_end)
            right = max(x_start, x_end)
            top = min(y_top, y_bottom)
            bottom = max(y_top, y_bottom)

            recorte = img[top:bottom, left:right]

            if recorte.size == 0:
                continue

            nombre_recorte = f'fila_{i}cuadro{j}.png'
            ruta_recorte = os.path.join(output_dir, nombre_recorte)
            cv2.imwrite(ruta_recorte, recorte)
            recortes.append(ruta_recorte)
            #print(f"Guardado recorte: {ruta_recorte}")

    """
    # Mostrar la imagen con los cuadros dibujados
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8, 12))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("Imagen con cuadros azules")
    plt.show()
    """
    return True 
