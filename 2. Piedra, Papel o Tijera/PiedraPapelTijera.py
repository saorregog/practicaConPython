# JUEGO DE PIEDRA, PAPEL O TIJERA

import random

options = ("Piedra", "Papel", "Tijera")

user_score = int(0)
pc_score = int(0)
round = int(1)

while (user_score < 3 and pc_score < 3):
    print("\n" + "*" * 10)
    print(f" RONDA {round}")
    print("*" * 10)

    valid_choice = False

    while (valid_choice == False):
        user_choice = input("\nElija Piedra, Papel o Tijera: ").capitalize()

        if(user_choice in options):
            valid_choice = True
    
    pc_choice = random.choice(options)

    print(f"\nEl usuario eligió {user_choice}")
    print(f"La máquina eligió {pc_choice}")

    if (user_choice == pc_choice):
        print("\n¡¡EMPATE!!")
    elif ((user_choice == "Piedra" and pc_choice == "Tijera") or (user_choice == "Papel" and pc_choice == "Piedra") or (user_choice == "Tijera" and pc_choice == "Papel")):
        user_score += 1
        print("\n¡¡EL USUARIO GANA!!")
    else:
        pc_score += 1
        print("\n¡¡EL USUARIO PIERDE!!")

    round += 1

    if (user_score == 3 or pc_score == 3):
        continue
    else:
        print(f"\nEl marcador es: Usuario {user_score} - Máquina {pc_score}")

print(f"\nEl marcador FINAL es: Usuario {user_score} - Máquina {pc_score}")

if (user_score == 3):
    print("\n=> EL USUARIO ES EL GANADOR DEL JUEGO <=\n")
else:
    print("\n=> LA MÁQUINA ES EL GANADOR DEL JUEGO <=\n")