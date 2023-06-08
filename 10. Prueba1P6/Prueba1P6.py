# DISEÑE UNA FUNCIÓN QUE RECIBA UN ARREGLO DE NÚMEROS ENTEROS Y LOS ORDENE DE MAYOR A MENOR SIN REPETIRLOS NÚMEROS.

def prueba_1_p6(arr):

    return sorted(set(arr), reverse=True)


print(prueba_1_p6([10, 2, 3, 4, -2, 4, 0]))
