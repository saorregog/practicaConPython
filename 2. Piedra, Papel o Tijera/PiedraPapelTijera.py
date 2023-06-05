# JUEGO DE PIEDRA, PAPEL O TIJERA

# FUNCIÓN DE ELECCIÓN DE OPCIONES
def choose_options():
    import random

    options = ("Piedra", "Papel", "Tijera")

    valid_choice = False

    while (valid_choice == False):
        user_choice = input("\nElija Piedra, Papel o Tijera: ").capitalize()

        if(user_choice in options):
            valid_choice = True
    
    pc_choice = random.choice(options)

    print(f"\nEl usuario eligió {user_choice}" , f"\nLa máquina eligió {pc_choice}")

    return user_choice, pc_choice

# FUNCIÓN DE PUNTUACIÓN
def score(user_choice, pc_choice):
    user_score = int(0)
    pc_score = int(0)

    if (user_choice == pc_choice):
        print("\n¡¡EMPATE!!")
    elif ((user_choice == "Piedra" and pc_choice == "Tijera") or (user_choice == "Papel" and pc_choice == "Piedra") or (user_choice == "Tijera" and pc_choice == "Papel")):
        user_score += 1
        print("\n¡¡EL USUARIO GANA!!")
    else:
        pc_score += 1
        print("\n¡¡EL USUARIO PIERDE!!")

    return user_score, pc_score

# FUNCIÓN DE EJECUCIÓN DE JUEGO
def run_game():
    round = int(1)

    user_global_score = int(0)
    pc_global_score = int(0)

    while (user_global_score < 3 and pc_global_score < 3):
        print("\n" + "*" * 10)
        print(f" RONDA {round}")
        print("*" * 10)
    
        user_choice, pc_choice = choose_options()

        user_score, pc_score = score(user_choice, pc_choice)

        user_global_score += user_score
        pc_global_score += pc_score

        round += 1

        if (user_global_score != 3 and pc_global_score != 3):
            print(f"\nEl marcador es: Usuario {user_global_score} - Máquina {pc_global_score}")
    
    return user_global_score, pc_global_score

# EJECUCIÓN DEL JUEGO
user_global_score, pc_global_score = run_game()

print(f"\nEl marcador FINAL es: Usuario {user_global_score} - Máquina {pc_global_score}")

if (user_global_score == 3):
    print("\n=> EL USUARIO ES EL GANADOR DEL JUEGO <=\n")
else:
    print("\n=> LA MÁQUINA ES EL GANADOR DEL JUEGO <=\n")
