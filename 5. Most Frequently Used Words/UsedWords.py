# VERSIÓN 1
def top_3_words(text):
    t_lowered = text.lower()

    for i in range(len(t_lowered)):
        if (i > 0 and i < (len(t_lowered) - 1) and t_lowered[i] == "'" and (t_lowered[i-1].isalpha() or t_lowered[i+1].isalpha())):
            t_lowered = t_lowered.replace(t_lowered[i], "4", 1)
        elif (not t_lowered[i].isalpha() and not t_lowered[i] == " "):
            t_lowered = t_lowered.replace(t_lowered[i], " ", 1)

    t_lowered = t_lowered.replace("4", "'").split()

    char_list = list(set(t_lowered))

    char_list_count = list()

    for i in range(len(char_list)):
        count = int(0)

        for j in range(len(t_lowered)):
            if (t_lowered[j] == char_list[i]):
                count += 1

        char_list_count.append(count)

    char_dict_count = {char_list[i]: char_list_count[i]
                       for i in range(len(char_list))}

    char_dict_count_sorted = dict(
        sorted(char_dict_count.items(), key=lambda e: e[1], reverse=True))

    return list(char_dict_count_sorted)[:3]


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))


# VERSIÓN 2
def top_3_words(text):
    t_lowered = text.lower()

    for i in range(len(t_lowered)):
        if (i > 0 and i < (len(t_lowered) - 1) and t_lowered[i] == "'" and (t_lowered[i-1].isalpha() or t_lowered[i+1].isalpha())):
            t_lowered = t_lowered.replace(t_lowered[i], "4", 1)
        elif (not t_lowered[i].isalpha() and not t_lowered[i] == " "):
            t_lowered = t_lowered.replace(t_lowered[i], " ", 1)

    t_lowered = t_lowered.replace("4", "'").split()

    char_set = set(t_lowered)

    char_dict_count = {char: t_lowered.count(char) for char in char_set}

    char_dict_count_sorted = dict(
        sorted(char_dict_count.items(), key=lambda e: e[1], reverse=True))

    return list(char_dict_count_sorted)[:3]


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))
