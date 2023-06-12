def justify(text, width):
    text = text.split()

    text_in_rows = list()

    while (len(text) > 0):
        row = str()
        for i in range(len(text)):
            if (len(row) + len(text[i]) + 1 <= width + 1):
                row += f"{text[i]} "
                text[i] = ""

                if (i < len(text) - 1):
                    continue

            text_in_rows.append(row)
            text = list(filter(lambda e: e != "", text))
            break

    text_in_rows = [list(" ".join(row.split())) for row in text_in_rows]

    for i in range(len(text_in_rows) - 1):
        pointer = int(1)

        if (" " in text_in_rows[i]):
            while (len(text_in_rows[i]) < width):
                for j in range(pointer, len(text_in_rows[i])):
                    if (text_in_rows[i][j] == " " and text_in_rows[i][j - 1] != " "):
                        text_in_rows[i].insert(j, " ")
                        pointer = j + 1
                        break

                if (j == len(text_in_rows[i]) - 1):
                    pointer = 1
        else:
            for j in range(width - len(text_in_rows[i])):
                text_in_rows[i].append(" ")

    text_in_rows = "\n".join(["".join(row) for row in text_in_rows])

    return text_in_rows

print(justify('123  45 6', 7))
print(justify(" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor. ", 15))
