def count_rect_triang1(points):
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if (points[i] and points[j] and points[i] == points[j]):
                points[j] = ""

    points = list(filter(lambda e: e != "", points))

    triangles = list()

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            for k in range(len(points)):
                if (k != i and k != j):
                    triangles.append([points[i], points[j], points[k]])

    for i in range(len(triangles) - 1):
        for j in range(i + 1, len(triangles)):
            if (triangles[i] and triangles[j]):
                count = int(0)

                for k in range(len(triangles[i])):
                    if (triangles[i][k] in triangles[j]):
                        count += 1

                if (count == 3):
                    triangles[j] = ""

    triangles = list(filter(lambda e: e != "", triangles))

    for i in range(len(triangles)):
        for j in range(len(triangles[i]) - 1):
            for k in range(j + 1, 3):
                l2 = (triangles[i][j][0] - triangles[i][k][0])**2 + (triangles[i][j][1] - triangles[i][k][1])**2
                triangles[i].append(l2)

    for triangle in triangles:
        for i in range(3):
            del triangle[0]

    count = int(0)

    for triangle in triangles:
        if (triangle[0] + triangle[1] == triangle[2] or triangle[0] + triangle[2] == triangle[1] or triangle[1] + triangle[2] == triangle[0]):
            count += 1

    return count

print(count_rect_triang1([[1, 2], [3, 3], [4, 1], [1, 1], [4, -1]]))
print(count_rect_triang1([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]))
print(count_rect_triang1([[30, 26], [36, 6], [12, 27], [9, 8], [9, 22], [6, 35], [26, 40],\
 [35, 18], [27, 2], [19, 18], [2, 41], [18, 3], [4, 37], [13, 25], [21, 34], [27, 45], [26, 12], [23, 16], [28, 1], [0, 25], [12, 25], [10, 41], [24, 18], [31, 38], [28, 17], [9, 23], [29, 1], [21, 43], [20, 46], [50, 10]]))


def count_rect_triang2(points):
    points = list(set(map(lambda e: tuple(e), points)))

    count = int(0)
    triangles = list()

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            for k in range(len(points)):
                if (k != i and k != j):
                    l2ij = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                    l2jk = (points[j][0] - points[k][0])**2 + (points[j][1] - points[k][1])**2
                    l2ik = (points[i][0] - points[k][0])**2 + (points[i][1] - points[k][1])**2

                    if (l2ij + l2jk == l2ik or l2ij + l2ik == l2jk or l2jk + l2ik == l2ij):
                        triangles.append([points[i], points[j], points[k]])

    triangles = set(map(lambda e: tuple(sorted(e)), triangles))

    return len(triangles)

print(count_rect_triang2([[1, 2], [3, 3], [4, 1], [1, 1], [4, -1]]))
print(count_rect_triang2([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]))
print(count_rect_triang2([[30, 26], [36, 6], [12, 27], [9, 8], [9, 22], [6, 35], [26, 40],\
 [35, 18], [27, 2], [19, 18], [2, 41], [18, 3], [4, 37], [13, 25], [21, 34], [27, 45], [26, 12], [23, 16], [28, 1], [0, 25], [12, 25], [10, 41], [24, 18], [31, 38], [28, 17], [9, 23], [29, 1], [21, 43], [20, 46], [50, 10]]))
