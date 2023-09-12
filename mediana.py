quantidade_valores = int(input('Numero de valores a serem inseridos: '))


valores = []

for i in range(quantidade_valores):
    valor = float(input(f'Insira os valores {i + 1}: '))
    valores.append(valor)

valores.sort()

def calcular_mediana(lista):
    n = len(lista)
    if n % 2 == 0:
        meio1 = lista[n // 2 - 1]
        meio2 = lista[n // 2]
        medianations = (meio1 + meio2) / 2
    else:
        medianations = lista[n // 2]
    return medianations

medianations = calcular_mediana(valores)


print(f"Mediana: {medianations:.3f}")

