from string import ascii_uppercase

print('Criptografar ou descriptografar?')
print('1-Criptografar')
print('2-Descriptografar')

x = int(input('Opção escolhida: '))

if x == 1:
    a = list(ascii_uppercase)
    cesar = int(input('Numero de posições a frente: '))
    m = input('Mensagem a ser criptografada: ')

    m = m.upper()
    mc = ""

    for l in m:
        i = ord(l) - 65
        if l in a:
            mc += a[(i + cesar) % 26]
        else:
            l
        print(f'Mensagem criptografada: {mc}')

elif x == 2:
    a = list(ascii_uppercase)
    cesar = int(input('Numero de posições atrás: '))
    m = input('Mensagem criptografada: ')

    m = m.upper()
    mc = ""

    for l in m:
        i = ord(l) - 65
        if l in a:
            mc += a[(i - cesar) % 26]
        else:
            l
        print(f'Mensagem descriptografada: {mc}')

else:
    print('Opção Inexistente')
