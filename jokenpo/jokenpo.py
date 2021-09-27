print("Bem-vindo ao JoKenPo! =)")
print(" Pedra = 0\n Papel = 1\n Tesoura = 2")
jogadorum = int(input("*Jogador 1 - Insira sua jogada:\n"))
jogadordois = int(input("*Jogador 2 - Insira sua jogada:\n"))

pedra = 0
papel = 1
tesoura = 2

if(jogadorum == 0) and (jogadordois == 0):
    print("Empate.")
elif(jogadorum == 0) and (jogadordois == 1):
    print("Vendedor: Jogador 2.")
elif(jogadorum == 0) and (jogadordois == 2):
    print("Vencedor: Jogador 1.")
elif(jogadorum == 1) and (jogadordois == 1):
    print("Empate.")
elif(jogadorum == 1) and (jogadordois == 0):
    print("Vencedor: Jogador 1.")
elif(jogadorum == 1) and (jogadordois == 2):
    print("Vencedor: Jogador 2.")
elif(jogadorum == 2) and (jogadordois == 2):
    print("Empate.")
elif(jogadorum == 2) and (jogadordois == 0):
    print("Vencedor: Jogador 2.")
elif(jogadorum == 2) and (jogadordois == 1):
    print("Vencedor: Jogador 1.")