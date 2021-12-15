############################################################################################################################
# # ATIVAR AMBIENTE #
# "C:\Users\altamiro.sousa\OneDrive\PARTICULAR\Cursos\Bootcampo - Eng.Dados\A003-Fundamentos_de_Ingestão_de_Dados\.venv\Scripts\activate.bat"
# ipython
############################################################################################################################


#%%
from typing import AsyncIterable
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#%%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'

#%%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)

#%%
soup

#%%
houses = soup.find_all(
    'a', {'class': 'property-card__content-link js-card-title'})
qtd_imoveis = float(
    soup.find('strong', {'class': 'results-summary__count'}).text.replace('.', ''))

#%%
len(houses)

#%%
qtd_imoveis / 36

#%%
houses = houses[0]

#%%
houses

#%%
df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'wlink',
    ]
)
i = 0

#%%
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f'valor i: {i} \t\t qtd_imoveis: {df.shape[0]}')
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    soup
    houses = soup.find_all(
        'a', {'class': 'property-card__content-link js-card-title'})
    for house in houses:
        try:
            descricao = houses.find(
                'span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try:
            endereco = houses.find(
                'span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = houses.find(
                'span', {'class': 'js-property-card-detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = houses.find(
                'li', {'class': 'property-card__detail-room'}).text.strip()
        except:
            quartos = None
        try:
            wc = houses.find(
                'li', {'class': 'property-card__detail-bathroom'}).text.strip()
        except:
            wc = None
        try:
            vagas = houses.find(
                'li', {'class': 'property-card__detail-garage'}).text.strip()
        except:
            vagas = None
        try:
            valor = houses.find(
                'div', {'class': 'property-card__price'}).text.strip()
        except:
            valor = None
        try:
            condominio = houses.find(
                'div', {'class': 'property-card__price-details--condo'}).text.strip()
        except:
            condominio = None
        try:
            wlink = 'https://www.vivareal.com.br' + houses['href']
        except:
            wlink = None

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink,
        ]

#%%
print(descricao)
print(endereco)
print(area + 'm²')
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(wlink)

#%%
df.to_csv('10-Dados_Imoveis_PT03-banco_de_imoveis.csv', sep=';', index=False)

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%
