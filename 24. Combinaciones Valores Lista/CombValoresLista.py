a = [1, 2, 3, 4]

b = list()

c = list()

result = list()

count = int(0)

while (count < len(a)):
    if (len(b) == 0):
        for i in range(len(a)):
            for j in range(len(a)):
                if (i != j):
                    b.append([a[i], a[j]])

        result.extend(b)
        count += 2
    else:
        for i in range(len(b)):
            for j in range(len(a)):
                if (a[j] not in b[i]):
                    comb = list()
                    comb = b[i].copy()
                    comb.append(a[j])
                    c.append(comb)

        b.clear()
        b.extend(c)
        result.extend(c)
        c.clear()
        count += 1

# FILTRAR DUPLICADOS

result = sorted(sorted(
    list(set(map(lambda e: tuple(sorted(e)), result)))), key=lambda e: len(e))

print(result)
