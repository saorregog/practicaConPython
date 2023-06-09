# VERSIÓN 1
def r2rightTriangle(strArr):
    if (len(strArr) <= 2):
        return 0

    strArr = [element.split(",") for element in strArr]

    strArr_x = list()
    strArr_y = list()

    for i in range(len(strArr) - 1):
        for j in range(i + 1, len(strArr)):
            if (strArr[j][0] == strArr[i][0]):
                for k in range(len(strArr)):
                    if (strArr[k][0] != strArr[i][0] and (strArr[k][1] == strArr[i][1] or strArr[k][1] == strArr[j][1])):
                        strArr_x.append([strArr[i], strArr[j], strArr[k]])

    for i in range(len(strArr) - 1):
        for j in range(i + 1, len(strArr)):
            if (strArr[j][1] == strArr[i][1]):
                for k in range(len(strArr)):
                    if (strArr[k][1] != strArr[i][1] and (strArr[k][0] == strArr[i][0] or strArr[k][0] == strArr[j][0])):
                        strArr_y.append([strArr[i], strArr[j], strArr[k]])

    strArr_2points = strArr_x + strArr_y

    for i in range(len(strArr_2points) - 1):
        for j in range(i + 1, len(strArr_2points)):
            if (strArr_2points[i] == [] or strArr_2points[j] == []):
                continue
            else:
                is_repeated = int(0)
                for k in range(3):
                    for l in range(3):
                        if (strArr_2points[i][k] == strArr_2points[j][l]):
                            is_repeated += 1
                if (is_repeated == 3):
                    strArr_2points[j] = []

    return len(list(filter(lambda e: e != [], strArr_2points)))
