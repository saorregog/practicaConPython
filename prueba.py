def top_3_words(text):
    t_lowered = text.lower()

    # t_l_revised = str()

    for i in range(len(t_lowered)):
        if (i > 0 and i < (len(t_lowered) - 1) and t_lowered[i] == "'" and t_lowered[i-1].isalpha() and t_lowered[i+1].isalpha()):
            t_lowered = t_lowered.replace(t_lowered[i], "4", 1)
        elif (not t_lowered[i].isalpha() and not t_lowered[i] == " "):
            t_lowered = t_lowered.replace(t_lowered[i], " ", 1)

    char_list = set(t_lowered.split())

    char_list_count = {char: t_lowered.count(char) for char in char_list}

    char_list_count_sorted = dict(
        sorted(char_list_count.items(), key=lambda e: e[1], reverse=True))

    return t_lowered
    # return list(char_list_count_sorted)[:3]


# print(top_3_words("  //wont won't won't "))
# print(top_3_words("  '''  "))
print(top_3_words("w'w,w"))