# DISEÑA UNA FUNCIÓN QUE IMPRIMA LAS PRIMERAS 10 FORMAS DEL PATRÓN.

def prueba_1_p1(num):
    d_l = list()  # digits_list
    d = num  # digit

    while (len(d_l) < 8):
        d += 1

        if (d == 10):
            d = 0

        d_l.append(d)

    return f"{d_l[0]}{d_l[1]}{d_l[2]},{d_l[7]}{num}{d_l[3]},{d_l[6]}{d_l[5]}{d_l[4]}".split(",")


print(prueba_1_p1(9))
