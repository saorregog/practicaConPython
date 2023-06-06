# CONVERTIR UN NÚMERO ENTERO EN NÚMERO BINARIO

def integer_to_binary(n):
    if (n // 2 > 1):
        b = integer_to_binary(round(n / 2)) + str(n % 2)
    else:
        b = str(n // 2) + str(n % 2)

    return b


print(integer_to_binary(41))
