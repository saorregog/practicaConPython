def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    text = "".join(text.lower().split())

    return " ".join([str(alphabet.find(letter) + 1) for letter in text if alphabet.find(letter) != -1])

print(alphabet_position("HOLA"))