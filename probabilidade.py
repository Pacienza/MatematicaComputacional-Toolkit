import scipy.stats as stats

media = int(input('Média de vida útil: '))
desvio = int(input('Desvio padrão: '))

print('Defina o intervalo de chances')
limite_inf = int(input('Limite inferior: '))
limite_sup = int(input('Limite Superior: '))

probabilidade = stats.norm.cdf(limite_sup, loc=media, scale=desvio) - stats.norm.cdf(limite_inf, loc=media, scale=desvio)

print(f'A probabilidade entre {limite_inf} e {limite_sup} é aproximadamente {probabilidade * 100:.2f}% ')
