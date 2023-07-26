#Bibliotecas importadas:

import requests
from bs4 import BeautifulSoup
from lxml import html

#Aplicação de funções:


def porcent(num):
  num = num.replace(',', '.')
  num = num.replace('%', '')
  num = float(num)
  num = num / 100

  return num


def ponto(pont):
  pont = pont.replace('.', '')
  pont = pont.replace(',', '.')
  pont = float(pont)

  return pont

def coleta_de_dados(infos):
    dados1 = []
    for info in infos:
        dados = info.find('div', attrs={'class': 'typography__body--2 typography--wmedium'})
        if dados is not None:
            dados1.append(dados.text.strip())

    for info in infos:
        dados = info.find('span', attrs={'class': 'typography__body--2 typography--wmedium'})
        if dados is not None:
            dados1.append(dados.text.strip())

    for valor in valrs:
        dados = valor.find('div', attrs={'class': 'cotacoes__header-price'})
        if dados is not None:
            dados1.append(dados.text.strip())
            
    return dados1


print('-'*25)
cod = str(input('Código do fundo: ')).upper()
invest = str(input('Valor a ser investido: R$'))
invest = invest.replace(',', '.')
invest = float(invest)
erro = str(input('Margem de erro em %: '))


url = f'https://www.infomoney.com.br/cotacoes/b3/fii/fundos-imobiliarios-'
response = requests.get(url + cod)
site = BeautifulSoup(response.text, 'html.parser')
infos = site.find_all('div', attrs={'class': 'cotacoes__yield-item'})
valrs = site.find_all('div', attrs={'class': 'cotacoes__header spacing--pt3 section-border--top'})


#Coletando dados

pop = coleta_de_dados(infos)

ultimo_rend = pop[0]
pvp = pop[1]
dy_mensal = pop[2]
dy_trimestral = pop[3]
dy_anual = pop[4]
price = pop[5]
price = price[:6]


#Apresentando informações

print('-'*25)
print('  COD               R$')
print(f'{cod}{price:>18}')
print('-'*25)
d = 'DIVIDEND YELD'
print(f'{d:^25}')
print(f'Mensal {dy_mensal:>18}\nTrimestral {dy_trimestral:>14}\nAnual {dy_anual:>19}')
print('-'*25)
i = 'INFORMES'
print(f'{i:^25}')
print(f'Ult. dividendo {ultimo_rend:>10}')
print(f'P/VP {pvp:>20}')


price = ponto(price)

#Calculando rendimentos com o DY

print('-'*25)
qnt = invest/price
qnt = int(qnt)
invest = price*qnt

erro_dec = porcent(erro)
mes_dec = porcent(dy_mensal)
tri_dec = porcent(dy_trimestral)
ano_dec = porcent(dy_anual)

rend_mes = ((invest*mes_dec)-(invest*mes_dec*erro_dec))
rend_tri = ((invest*tri_dec)-(invest*tri_dec*erro_dec))
rend_ano = ((invest*ano_dec)-(invest*ano_dec*erro_dec))

print(f'Ultilizando a margem de \nerro de {erro}% chegamos \naos redimentos abaixo:\n')
print(f'Quantidade de cotas: {qnt}')
print(f'Rendimento (a.m.) R${rend_mes:.2f}')
print(f'Rendimento (a.t.) R${rend_tri:.2f}')
x = (f'Rendimento (a.a.) R${rend_ano:.2f}')
print(x)
print('-'*len(x))
