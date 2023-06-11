# FALTA ORDENAR LOS RESULTADOS PRIORIZANDO PRIMER TÉRMINO ( : 1 2) Y LUEGO NÚMERO DE VECES QUE CADA LETRA SE REPITE

def mix(s1, s2):
    s1 = "".join([char for char in s1 if char.isalpha() and char.islower()])
    s2 = "".join([char for char in s2 if char.isalpha() and char.islower()])

    s_ = set(s1)

    for letter in set(s2):
        s_.add(letter)

    s_ = sorted(list(s_), reverse=False)

    result = list()

    for letter in s_:
        if (s1.count(letter) > s2.count(letter) and s1.count(letter) > 1):
            result.append(["1", letter, s1.count(letter)])
        elif (s2.count(letter) > s1.count(letter) and s2.count(letter) > 1):
            result.append(["2", letter, s2.count(letter)])
        elif (s1.count(letter) == s2.count(letter) and s1.count(letter) > 1):
            result.append(["=", letter, s2.count(letter)])

    result = sorted(result, key=lambda e: e[2], reverse=True)

    result_s = "/".join([f"{element[0]}:{element[1] * element[2]}" for element in result])

    return result_s

print(mix("A generation must confront the looming ", "codewarrs"))