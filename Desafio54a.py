# Conta quantos são os maiores e menores de idade com base no ano de nascimento.
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo, temos \033[34m{}\033[m pessoa(s) maior(es) de idade e \033[34m{}\033[m pessoa(s) menor(es) de idade.'
      .format(maior, menor))
