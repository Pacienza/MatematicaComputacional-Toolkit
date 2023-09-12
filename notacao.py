numero = float(input("Digite o número: "))
expoente = int(input("Digite o expoente: "))


resultado = numero * (10 ** expoente)


casas_decimais = int(input("Digite a quantidade de casas decimais desejadas: "))


formato = f'%.{casas_decimais}e'


print(formato % resultado)
