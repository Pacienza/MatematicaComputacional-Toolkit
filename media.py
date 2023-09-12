quantidade_valores = int(input('Numero de valores a serem inseridos: '))

valores = []

for i in range(quantidade_valores):
    valor = float(input(f'Insira o valor {i + 1}: '))
    valores.append(valor)

def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

media = calcular_media(valores)

print(f'Média: {media}')