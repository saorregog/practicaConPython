def max_sequence(arr):
    max = int(0)
    acum = int(0)

    for number in arr:
        acum += number

        if (acum > max):
            max = acum

        if (acum < 0):
            acum = 0

    return max

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
