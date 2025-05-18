from NN.funcionComparacion import comparar_imagen 
from NN.rotacion import estimate_rotation

def image_info(pos):
    img = "temp.png"
    best_score, anaquel, charola, posicion, orientation = comparar_imagen(img)
    angulo = estimate_rotation(pos)
    actual_pos = anaquel + "," +  charola + "," + posicion
    orientations = {"1": "costado derecho", "2": "costado izquierdo", "3": "detrás", "4": "arriba", "5": "abajo"}

    if (actual_pos != pos):
        return {"ans": "El producto no es el que se espera",
                "angle": angulo,
                "pos": actual_pos }
    else:
        return {"ans": "El producto está bien colocado", "angle": angulo,"pos": actual_pos }
    
    
