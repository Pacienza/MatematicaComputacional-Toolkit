x1 = float(input('Digite o valor EXATO da variável: '))
x2 = float(input('Digite o valor APROXIMADO da variável: '))

EA = abs(x2 - x1)
ER = abs(EA)/abs(x1)

print('Erro Relativo: ', ER)