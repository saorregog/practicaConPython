def valid_braces(string):
    support_list = list()

    for i in range(len(string)):
        if (i == 0 and string[i] in ")]}"):
            return False

        if (string[i] in "([{"):
            support_list.append(string[i])
            continue

        if (len(support_list) == 0):
            return False
        
        if (string[i] == ")" and support_list[- 1] == "("):
            support_list.pop()
        elif (string[i] == "]" and support_list[- 1] == "["):
            support_list.pop()
        elif (string[i] == "}" and support_list[- 1] == "{"):
            support_list.pop()
        else:
            return False
    
    return len(support_list) == 0

print(valid_braces(")((((((((((("))