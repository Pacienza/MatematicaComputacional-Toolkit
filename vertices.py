print('Calculo das Coordenadas do vértice da parábola')
print('Insira os valores da função quadrática')

a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

xv = -b / (2 * a)
delta = b ** 2 - 4 * a * c
yv = -delta / (4 * a)

print(f'Xv = {xv} e Yv = {yv}')
