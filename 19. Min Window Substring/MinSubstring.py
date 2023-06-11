def MinWindowSubstring(strArr):
    k = strArr[0]
    n = strArr[1]

    result = list()

    for i in range(len(k)):
        for j in range(len(k), len(n) - 1 + i, -1):
            copy_k = k[i:j]
            is_in = True

            for letter in n:
                if (letter not in copy_k):
                    is_in = False
                    break
                else:
                    copy_k = copy_k.replace(letter, "", 1)

            if (is_in):
                result.append(k[i:j])

    return sorted(result, key=lambda e: len(e), reverse=False)[0]

print(MinWindowSubstring(["aaabaaddae", "aed"]))
