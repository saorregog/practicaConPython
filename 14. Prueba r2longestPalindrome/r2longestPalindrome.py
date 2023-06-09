# VERSIÓN 1
def r2longestPalindrome(strParam):
    strParam = strParam.lower().split()
    strParam = "".join(strParam)

    result = list()

    for i in range(len(strParam)):
        for j in range(len(strParam), i, -1):
            str_reversed = strParam[i:j]
            if (str_reversed[::-1] in strParam):
                result.append(len(str_reversed))

    return max(result)


print(r2longestPalindrome(
    "anitalavalatinaanitalavalatinaanitalavalatinaanitalavalatina"))
