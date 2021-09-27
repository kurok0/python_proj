from typing import List


print('Bem-vindo(a) à minha calculadora.')
print('Fiz este projeto para me ajudar na organização de minha rendas.')

rendamensal = float(input('Insira o valor total de sua renda mensal: '))
print('Excelente! Vamos então listar seus gastos mensais.')
print('***MÁXIMO DE 3 POR VEZ!!!!!***')

nome = str(input('Nome da instituição ou preferencial: '))
div = float(input('Valor: '))
nome1 = str(input('Nome da instituição ou preferencial: '))
div1 = float(input('Valor: '))
nome2 = str(input('Nome da instituição ou preferencial: '))
div2 = float(input('Valor: '))

print('Essa é a sua lista de gastos.')
gasto = [f'{nome} = R${div}', f'{nome1} = R${div1}', f'{nome2} = R${div2}']
print(gasto)

print('Vamos calcular?')

print('Nosso primeiro cálculo será: ', f'{nome}' + '.')
total = float(rendamensal - div)
print('O resultado é:', f'{total}' + '.')
print('Continuando...')

total1 = float(total - div1)
print('O resultado é:', f'{total1}' + '.')
print('Continuando...')

total2 = float(total1 - div2)
print('O resultado é:', f'{total2}' + '.')

if(total2 > 0):
    print('Você terminou no azul! Parabéns! Agora guarde e invista seu dinheiro.')
elif(total2 == 0):
    print('Quase. Se segura o resto do mês!')
else:
    print('Tá endividado mais ainda parça.')