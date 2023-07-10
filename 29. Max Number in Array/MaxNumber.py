def max_number(list):

    if (len(list) == 0):
        return 0
    elif (len(list) == 1):
        return list[0]
    else:
        if (list[len(list) - 1] > max_number(list[:len(list) - 1])):
            return list[len(list) - 1]
        else:
            return max_number(list[:len(list) - 1])


print(max_number([1, 50, -8, 3, 25]))
