# DISEÑE UNA FUNCIÓN QUE RECIBA COMO ARGUMENTO UN NÚMERO ENTERO POSITIVO DE 11 DÍGITOS Y EXTRAE LA FECHA DE NACIMIENTO RETORNÁNDOLA COMO STRING.

def prueba_1_p4(num):
    string_num = str(num)

    year = string_num[:2]
    month = string_num[2:4]
    day = string_num[4:6]

    month_year = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre",
    }

    return f"Nacimiento el {int(day)} de {month_year[month]} de 19{year}"


print(prueba_1_p4(99120199999))
