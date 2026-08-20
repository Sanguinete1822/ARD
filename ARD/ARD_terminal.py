# A.R.D. (3)
import random

valid_plays = ['rec', 'def', 'shoot']
player_damage = 0
pc_damage = 0
player_ammunition = 0
pc_ammunition = 0
print("rec = recarregar, def = defender, shoot = atirar")
while player_damage < 1 and pc_damage < 1:
    print("")
    player_choice = input("  Você escolhe: recarregar, defender or atirar? ")
    pc_choice = random.choice(valid_plays)
    print(f"você escolheu {player_choice}, e o CPU escolheu {pc_choice}")

    if player_choice == 'def':
        print(f"-Munição do Jogador:{player_ammunition}")
    if pc_choice == 'def':
        print(f"-Munição do CPU:{pc_ammunition}")

    if player_choice == 'rec':
        player_ammunition += 1
        print(f"-Munição do Jogador: {player_ammunition}")
    if pc_choice == 'rec':
        pc_ammunition += 1
        print(f"-Munição do CPU: {pc_ammunition}")

    if pc_choice == 'shoot' and pc_ammunition < 1:
        print(f"-Sem munição")
    if player_choice == 'shoot' and player_ammunition < 1:
        print("-Sem munição")

    if player_choice == 'shoot' and player_ammunition > 0 and pc_choice != 'def' and pc_choice != 'shoot':
        pc_damage = + 1
#aqui :and pc_choice != 'shoot'
        print("CPU perdeu... Você ganhou!!")
    elif player_choice == 'shoot' and player_ammunition > 0 and pc_choice == 'def':
        player_ammunition -= 1
        print(f"-Munição do Jogador: {player_ammunition}")
        print("CPU se defendeu")

    if pc_choice == 'shoot' and pc_ammunition > 0 and player_choice != 'def' and player_choice != 'shoot':
        player_damage = + 1
#e aqui :and player_choice != 'shoot'
        print("CPU ganhou!! Você perdeu...")
    elif pc_choice == 'shoot' and pc_ammunition > 0 and player_choice == 'def':
        pc_ammunition -= 1
        print(f"-Munição do CPU: {pc_ammunition}")
        print("Você defendeu")

    if pc_choice == 'shoot' and player_choice == 'shoot' and pc_ammunition > 0 and player_ammunition > 0:
        print("Os dois perderam")
        player_damage = + 1
        pc_damage = + 1