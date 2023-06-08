# DISEÑE UNA FUNCIÓN QUE RECIBA UNA CADENA DE TEXTO Y RETORNE CUÁNTAS PALABRAS COMIENZAN POR LA LETRA "a".

def prueba_1_p8(str):

    return len([word for word in str.lower().split() if word.startswith("a")])


print(prueba_1_p8("a A bbb aA aa Ax az"))
