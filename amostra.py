from math import ceil

N = int(input('Tamanho da população de dados: '))
E = float(input('Margem de erro(em %): '))
e = E / 100

n = ceil(N / (1 + N * e ** 2))

print(f'Tamanho da amostra: {n}')
