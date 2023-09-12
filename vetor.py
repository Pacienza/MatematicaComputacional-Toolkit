import numpy as np

print('Multiplicar Vetor ou obter média(U.V) ')
print('1-Multiplicar | 2- Somar | 3- Subtrair | 4-Média')
opcao = int(input('Opção desejada: '))

if opcao == 1:
    quantidade_dados = int(input('Quantidade de valores no vetor: '))
    dados = []

    for i in range(quantidade_dados):
        dado = float(input(f'Insira os valores {i + 1}: '))
        dados.append(dado)

    v = np.array([dados])
    m = float(input('Valor multiplicador: '))
    w = m * v

    print(w)

elif opcao == 2:
    quantidade_dados1 = int(input('Quantidade de valores no primeiro vetor: '))
    dados1 = []

    for i in range(quantidade_dados1):
        dado1 = float(input(f'Insira os valores {i + 1}: '))
        dados1.append(dado1)

    quantidade_dados2 = int(input('Quantidade de valores no segundo vetor: '))
    dados2 = []

    for i in range(quantidade_dados2):
        dado2 = float(input(f'Insira os valores {i + 1}: '))
        dados2.append(dado2)

    u = np.array([dados1])
    v = np.array([dados2])
    w = u + v

    print(w)

elif opcao == 3:
    quantidade_dados1 = int(input('Quantidade de valores no primeiro vetor: '))
    dados1 = []

    for i in range(quantidade_dados1):
        dado1 = float(input(f'Insira os valores {i + 1}: '))
        dados1.append(dado1)

    quantidade_dados2 = int(input('Quantidade de valores no segundo vetor: '))
    dados2 = []

    for i in range(quantidade_dados2):
        dado2 = float(input(f'Insira os valores {i + 1}: '))
        dados2.append(dado2)

    u = np.array([dados1])
    v = np.array([dados2])
    w = u - v

    print(w)

elif opcao == 4:
    quantidade_dados1 = int(input('Quantidade de valores no primeiro vetor: '))
    dados1 = []

    for i in range(quantidade_dados1):
        dado1 = float(input(f'Insira os valores {i + 1}: '))
        dados1.append(dado1)

    quantidade_dados2 = int(input('Quantidade de valores no segundo vetor: '))
    dados2 = []

    for i in range(quantidade_dados2):
        dado2 = float(input(f'Insira os valores {i + 1}: '))
        dados2.append(dado2)

    u = np.array([dados1])
    v = np.array([dados2])
    w = np.inner(u, v)

    print(w)
