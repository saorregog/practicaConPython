def mix(s1, s2):
    s1 = "".join(s1.lower().split())
    s_1 = list(s1)
    s1_ = list(set(s1))
    
#     s2 = "".join(s1.lower().split())
    s2 = sorted(list("".join(s2.lower().split())), reverse=False)
    s2_ = list(set(s1))
    
    string1 = sorted([[letter, s1.count(letter)] for letter in s1_ if s1.count(letter) > 1], key=lambda e: e[1], reverse=True)
    string2 = sorted([[letter, s2.count(letter)] for letter in s2_ if s2.count(letter) > 1], key=lambda e: e[1], reverse=True)
    
    result = list()
    
    return s2