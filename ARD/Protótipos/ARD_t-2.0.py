import random
validos = ['at' , 'rec' , 'def'] # ações válidas
# variáveis ativas
vida_jogador = 1
vida_pc = 1
balas_jogador = 0
balas_pc = 0
#começo
print("Para Recarregar:rec; defender:def; atirar:at")
while vida_jogador == 1 and vida_pc == 1: #jogatina conditional infinity
    print(" ")
    escolha_j = input("Escolha sua jogada:")
    escolha_pc = random.choice(validos)
    print("Você:", escolha_j , "Computador:", escolha_pc)
    if escolha_j == 'rec':
        balas_jogador += 1
    if escolha_pc == 'rec':
        balas_pc += 1
    if escolha_j == 'at':
        if balas_jogador > 0:
            if escolha_pc != 'def':
                if escolha_pc != 'at' or balas_pc < 1:
                    balas_jogador -=1
                    vida_pc -= 1
                    print("você ganhou")
            else:
                balas_jogador -= 1
                print("defendido")
        elif balas_jogador == 0:
            print("Sem Munição")
    if escolha_pc == 'at':
        if balas_pc > 0:
            if escolha_j != 'def':
                if escolha_j != 'at' or balas_jogador < 1:
                    balas_pc -= 1
                    vida_jogador -= 1
                    print("você perdeu")
            else:
                balas_pc -= 1
                print("você defendeu")
        elif balas_pc == 0:
            print("Computador sem Munição")
    print(f"Você:{balas_jogador}") # munição
    print(f"Computador:{balas_pc}")
    if escolha_j =='at' and escolha_pc == 'at':
        if balas_jogador > 0  and balas_pc > 0:
            vida_jogador -= 1
            vida_pc -= 1
            print("Tiro duplo!!!")