import json
from NN.funcionComparacion import funcionComparacion
from NN.rotacion import estimate_rotation
from NN.chopper import chop_image

def get_info(path, pos, shelf=0):
    error = False

    best_score, anaquel, charola, posicion, orientation = funcionComparacion(path)
    angulo = estimate_rotation(pos + str(shelf))
    best_em = anaquel + "," +  charola + "," + posicion

    if (best_em != pos):
        if(shelf != 0):
            info = "El producto no está en la orientación esperada"
        else:
            info = "El producto no es el que se espera"
        error = True
    elif (abs(angulo) > 45):
        info = f"El producto esta mal colocad con angulo: {angulo}"
        error = True
    else:
        info = "El producto está bien colocado"
        error = False
    
    return (error, info)
    
def handle_request(json_data):
    ans = {}
    a = 0 
    dic = json.loads(json_data)
    img = "temp.png"
    shelf = dic["shelf"]

    if dic["once"] == 1:
        return get_info(img, dic["pos"])
    
    limits = [7,6,8,6] if shelf == 0 else [4,4,8,7]
    
    for i in range(1, len(limits) + 1):
        for j in range(1,limits[i] + 1):

            path = f"fila_{i}cuadro{j}.png"
            error,info = get_info(path, pos= str(shelf) + "," + str(i)+  "," + str(j))  

            if not error:
                continue
            else:
                a+= 1
                ans[str(a)] = info
            
    return ans  
    
    