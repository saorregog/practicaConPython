# VERSIÓN 1
def r2longestPalindrome1(strParam):
    strParam = strParam.lower().split()
    strParam = "".join(strParam)

    result = list()

    for i in range(len(strParam)):
        for j in range(len(strParam), i, -1):
            str_reversed = strParam[i:j]
            if (str_reversed[::-1] in strParam):
                result.append(len(str_reversed))

    return max(result)

print(r2longestPalindrome1(
    "anitalavalatinaanitalavalatinaanitalavalatinaanitalavalatina"))


# VERSIÓN 2
def r2longestPalindrome2(strParam):
    strParam = strParam.lower().split()
    strParam = "".join(strParam)

    result = int(0)

    for i in range(len(strParam)):
        for j in range(len(strParam), i, -1):
            str_reversed = strParam[i:j]
            if (str_reversed[::-1] in strParam and len(str_reversed) > result):
                result = len(str_reversed)

    return result

print(r2longestPalindrome2(
    "anitalavalatinaanitalavalatinaanitalavalatinaanitalavalatina"))
