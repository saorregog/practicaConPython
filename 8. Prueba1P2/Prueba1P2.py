# DISEÑA UNA FUNCIÓN QUE RECIBA COMO PARÁMETRO UN NÚMERO ENTERO POSITIVO Y RETORNA EL NÚMERO DE LA SECUENCIA DE FIBONACCI QUE ES ESTRICTAMENTE MENOR QUE ÉL.

def prueba_1_p2(num):
    old_fib = 0
    fib = 1
    new_fib = int()

    while (fib < num):
        new_fib = fib + old_fib
        old_fib = fib
        fib = new_fib

    return old_fib


print(prueba_1_p2(35))
