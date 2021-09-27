import random

print("Este é um gerador de senhas.")
print("Escolha a quantidade de caracteres de sua senha:")

lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simb = "#@!$%&"
num = "1234567890"

def keybase():
    return lc+uc+simb+num

def senha(y):
    print(''.join(random.choice(keybase()) for i in range(y)))

senha(int(input()))
