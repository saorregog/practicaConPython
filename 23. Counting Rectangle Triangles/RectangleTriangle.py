def count_rect_triang(points):
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

print(count_rect_triang([[1, 2], [3, 3], [4, 1], [1, 1], [4, -1]]))
print(count_rect_triang([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]))
print(count_rect_triang([[30, 26], [36, 6], [12, 27], [9, 8], [9, 22], [6, 35], [26, 40],\
 [35, 18], [27, 2], [19, 18], [2, 41], [18, 3], [4, 37], [13, 25], [21, 34], [27, 45], [26, 12], [23, 16], [28, 1], [0, 25], [12, 25], [10, 41], [24, 18], [31, 38], [28, 17], [9, 23], [29, 1], [21, 43], [20, 46], [50, 10]]))


# a = [[12, 27], [19, 18], [21, 34]]
# # a = [[30, 26], [21, 34], [13, 25]]

# sij = round((a[0][1] - a[1][1]) / (a[0][0] - a[1][0]), 2)
# sik = round((a[0][1] - a[2][1]) / (a[0][0] - a[2][0]), 2)
# sjk = round((a[1][1] - a[2][1]) / (a[1][0] - a[2][0]), 2)

# print(sik == round((-1 / sij), 2) or sjk == round((-1 / sij), 2))