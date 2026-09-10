import random
import tkinter as tk
janela = tk.Tk()
BT = tk.Button
botoes = []
plam = cpuam = 0
plays = 0
def exit():
    janela.destroy()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
def jogar(escolha):
    atualizar2("Escolha:")
    global plam, cpuam, plays
    if escolha == 'atirar':
        plays =  ['defender'] * 12 +['recarregar'] * 3 +['atirar'] * 5
    elif escolha == 'recarregar':
        plays = ['defender'] * 3 +['recarregar'] * 5 +['atirar'] * 12
    else:
        plays = ['defender'] * 5 +['recarregar'] * 12 +['atirar'] * 3

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
        else: return atualizar2("Sem Munição!!")
    if pc == 'atirar':
        if cpuam > 0:
            cpuam -= 1
            if escolha != 'defender': return fim("Computador venceu")
        elif escolha == 'atirar':
            if plam > 0:
                fim("Os dois perderam")
        else: return atualizar2("Computador sem Munição!!")
    atualizar(f"Você:{escolha} | PC:{pc}   "
              f"   munição {plam}/{cpuam}")
def atualizar(txt):
    label.config(text=txt)
def atualizar2(txt):
    label2.config(text=txt)
def fim(txt):
    label.config(text=txt)
    for b in botoes:
        b.config(state="disabled")
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
botaosaida.pack()
janela.mainloop()
