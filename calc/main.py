
from typing import List


print('Bem-vindo(a) à minha calculadora.')
print('Fiz este projeto para me ajudar na organização de minha rendas.')

rendamensal = float(input('Insira o valor total de sua renda mensal: '))
print('Excelente! Vamos então listar seus gastos mensais.')

class Calc:
    def proj(self, instit, divd):
        self.instit = instit
        self.divd = divd

    def toString(self):
        return f'{self.instit} {self.divd}'

class Main:
    lista = []

    def adicionarLista(object):
        Main.lista.append(object)
        input(str("Insira o nome da instituição ou de sua preferência: "))
        divd = print("Valor: "), float(input())

        instit = Main()
        instit.Calc()

Main.adicionarLista()
print('Essa é a sua lista de gastos.')
print(Main.lista)

## **AINDA VOU EDITAR, CÓDIGO ANTIGO...**
##print('Vamos calcular?')
##print('Nosso primeiro cálculo será: ', f'{calc()}' + '.')
##total = float(rendamensal - calc())
##print('O resultado é:', f'{total}' + '.')
##print('Continuando...')