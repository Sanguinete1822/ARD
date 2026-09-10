import random
import tkinter as tk
janela = tk.Tk()
BT = tk.Button
botoes = []
plam = cpuam = 0
plays = 0
n = 1
def reset ():
    global n,plam,cpuam,plays
    plays = 0
    n = 1
    plam = cpuam = 0
    label.config(text="Bem vindo")
    label2.config(text="Escolha:")
    [b.config(state="normal") for b in botoes]
    denovo.pack_forget()
def exit():
    janela.destroy()
def jogar(escolha):
    atualizar2("Escolha:")
    global plam, cpuam, plays
    if escolha == 'atirar':
        if plam > 0 and cpuam > 0:
            if cpuam > 1:
                plays = ['defender'] * 90 + ['atirar'] * 10
            else:
                plays = ['defender'] * 90 + ['recarregar'] * 1 + ['atirar'] * 9
        elif plam > 0 and cpuam == 0:
            plays = ['defender'] * 90 + ['recarregar'] * 10
        elif plam == 0 and cpuam > 0:
            if cpuam > 1:
                plays = ['recarregar'] * 5 + ['atirar'] * 95
            else:
                plays = ['recarregar'] * 10 + ['atirar'] * 90
        elif plam == 0 and cpuam == 0:
            plays = ['recarregar'] * 90 + ['atirar'] * 10
    elif escolha == 'recarregar':
        if cpuam == 0:
            plays = ['recarregar'] * 90 + ['atirar'] * 10
        elif cpuam > 1:
            plays =  ['recarregar'] * 5 + ['atirar'] * 95
        else:
            plays = ['recarregar'] * 10 + ['atirar'] * 90
    else:
        plays = ['recarregar'] * 90 +['atirar'] * 10
    pc = random.choice(plays)
    if escolha == 'recarregar': plam += 1
    if pc == 'recarregar': cpuam += 1
    if escolha == 'atirar':
        if plam > 0:
            plam -= 1
            if pc != 'defender': return fim("Jogador venceu")
        elif pc == 'atirar':
            if cpuam > 0:
                fim("Os dois perderam")
        else: atualizar2("Sem Munição!!")
    if pc == 'atirar':
        if cpuam > 0:
            cpuam -= 1
            if escolha != 'defender': return fim("Computador venceu")
        elif escolha == 'atirar':
            if plam > 0:
                fim("Os dois perderam")
        else: atualizar2("Computador sem Munição!!")
    atualizar(f"Você:{escolha} | PC:{pc}   munição {plam}/{cpuam}")
    global n
    print("Rodada" , n)
    n += 1
    print(f"Você: {escolha} | PC: {pc}")
    print(f"munição {plam}/{cpuam}")
    return n
def atualizar(txt):
    label.config(text=txt)
def atualizar2(txt):
    label2.config(text=txt)
def fim(txt):
    label.config(text=txt)
    for b in botoes:
        b.config(state="disabled")
    denovo.pack()
titulo = janela.title("A.R.D.")
janela.geometry("300x300")
label = tk.Label(janela, text="Bem Vindo")
label.pack()
label2 = tk.Label(janela, text="Escolha:")
label2.pack()
jogadas = ['atirar','recarregar','defender' ]
for t in jogadas:
    b = BT(janela, text=t, command = lambda x=t: jogar(x))
    botoes.append(b)
    b.pack()
botaosaida = BT(text="Parar tudo", command=exit )
denovo = BT(janela, text="tentar de novo", command=reset)
botaosaida.pack()
janela.mainloop()
