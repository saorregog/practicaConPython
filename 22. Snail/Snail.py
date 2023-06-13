def snail(snail_map):
    result = list()

    while (len(snail_map)):
        for i in range(len(snail_map[0])):
            result.append(snail_map[0][i])

        del snail_map[0]

        if (len(snail_map)):
            for i in range(len(snail_map)):
                result.append(snail_map[i][-1])
                snail_map[i].pop()
        else:
            return result

        if (len(snail_map)):
            for i in range(len(snail_map[-1]) - 1, -1, -1):
                result.append(snail_map[-1][i])

            del snail_map[-1]
        else:
            return result

        if (len(snail_map)):
            for i in range(len(snail_map) - 1, -1, -1):
                result.append(snail_map[i][0])
                snail_map[i].pop(0)
        else:
            return result

    return result

print(snail([[1,  2,  3,  4,  5,  6],
             [20, 21, 22, 23, 24,  7],
             [19, 32, 33, 34, 25,  8],
             [18, 31, 36, 35, 26,  9],
             [17, 30, 29, 28, 27, 10],
             [16, 15, 14, 13, 12, 11]]))
