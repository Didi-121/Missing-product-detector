from NN.funcionComparacion import funcionComparacion
from NN.rotacion import estimate_rotation

def image_info(pos):
    img = "temp.png"
    best_score, anaquel, charola, posicion, orientation = funcionComparacion(img)
    angulo = estimate_rotation(img, pos)
    actual_pos = anaquel + "," +  charola + "," + posicion
    orientations = {"1": "costado derecho", "2": "costado izquierdo", "3": "detrás", "4": "arriba", "5": "abajo"}

    if (actual_pos != pos):
        return {"ans": "El producto no es el que se espera",
                "pos": actual_pos }
    elif (orientation != 0):
        return {"ans": "El producto no está en la orientación esperada",
                "pos": orientations[orientation]}
    elif (angulo > 45):
        return {"ans": "El producto esta mal colocado", 
                "angle": angulo}
    else:
        return {"ans": "El producto está bien colocado"}
    
    