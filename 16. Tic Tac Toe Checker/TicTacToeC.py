def is_solved(board):
    for row in board:
        if (row == [1, 1, 1]):
            return 1 # 1 GANA
        elif (row == [2, 2, 2]):
            return 2 # 2 GANA

    for column in [[board[0][i], board[1][i], board[2][i]] for i in range(3)]:
        if (column == [1, 1, 1]):
            return 1 # 1 GANA
        elif (column == [2, 2, 2]):
            return 2 # 2 GANA

    count1 = list()
    count2 = list()

    for i in range(3):
        count1.append(board[i][i])
        count2.append(board[i][len(board) - 1 - i])

    if (count1 == [1, 1, 1] or count2 == [1, 1, 1]):
        return 1 # 1 GANA
    elif (count1 == [2, 2, 2] or count2 == [2, 2, 2]):
        return 2 # 2 GANA

    for pos in board:
        for i in range(3):
            if (pos[i] == 0):
                return -1 # JUEGO ABIERTO

    return 0 # EMPATE

print(is_solved([[1, 2, 1],
                 [1, 1, 2],
                 [2, 2, 0]]))
