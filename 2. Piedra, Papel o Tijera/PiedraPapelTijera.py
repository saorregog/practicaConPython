# JUEGO DE PIEDRA, PAPEL O TIJERA

import random

options = ("Piedra", "Papel", "Tijera")

user_option = input("Elija Piedra, Papel o Tijera: ").capitalize()
pc_option = random.choice(options)

print(f"\nEl usuario eligió {user_option}")
print(f"La máquina eligió {pc_option}\n")

if (user_option == pc_option):
    print("¡¡EMPATE!!")
elif ((user_option == "Piedra" and pc_option == "Tijera") or (user_option == "Papel" and pc_option == "Piedra") or (user_option == "Tijera" and pc_option == "Papel")):
    print("¡¡EL USUARIO GANA!!")
else:
    print("¡¡EL USUARIO PIERDE!!")
