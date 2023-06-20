def next_bigger(n):
    if (len(str(n)) == 1):
        return -1

    m = n
    m = list(str(m))

    index = int(-2)

    for i in range(len(m) - 1, 0, -1):
        if (m[i] > m[i - 1]):
            index = i - 1
            break

    if (index == -2):
        return -1

    m_ = m[index:]

    aux1 = list()
    aux2 = list()
    result = list()
    count = int(1)

    while (count < len(m_)):
        if (count == 1):
            for i in range(len(m_)):
                for j in range(len(m_)):
                    if (i != j and [m_[i], m_[j]] not in aux1):
                        aux1.append([m_[i], m_[j]])

            count += 1

            if (count == len(m_)):
                result.extend(aux1)
        else:
            for i in range(len(aux1)):
                for j in range(len(m_)):
                    temp = aux1[i].copy()
                    temp.append(m_[j])
                    if (temp not in aux2 and temp.count(m_[j]) <= m_.count(m_[j])):
                        aux2.append(temp)

            count += 1

            if (count == len(m_)):
                result.extend(aux2)

            aux1.clear()
            aux1.extend(aux2)
            aux2.clear()

    result.sort()

    result = m[:index] + result[result.index(m_) + 1]

    return int("".join(result))

print(next_bigger(2017))
print(next_bigger(59884848459853))
