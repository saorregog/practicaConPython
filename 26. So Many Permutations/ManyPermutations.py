def permutations(s):
    if (len(s) == 1):
        return list(s)

    aux1 = list()
    aux2 = list()

    result = list()

    count = int(1)

    while (count < len(s)):

        if (count == 1):
            for i in range(len(s)):
                for j in range(len(s)):
                    if ([s[i], s[j]] not in aux1 and [s[i], s[j]].count(s[j]) <= s.count(s[j])):
                        aux1.append([s[i], s[j]])

            if (count == len(s) - 1):
                result.extend(aux1)

            count += 1

        else:
            for i in range(len(aux1)):
                for j in range(len(s)):
                    if (aux1[i].count(s[j]) == s.count(s[j])):
                        continue
                    else:
                        temp = aux1[i].copy()
                        temp.append(s[j])
                        if (count != len(s) - 1):
                            aux2.append(temp)
                        else:
                            result.append(temp)

            count += 1

            aux1.clear()
            aux1.extend(aux2)
            aux2.clear()

    result = list(map(lambda e: list(e), list(
        set(map(lambda e: tuple(e), result)))))

    return ["".join(element) for element in result]

print(permutations("ab"))
