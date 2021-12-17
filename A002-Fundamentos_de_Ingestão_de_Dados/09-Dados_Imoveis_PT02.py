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

#%%property-card
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
descricao = houses.find('span', {'class': 'property-card__title'}).text.strip()
print(descricao)

endereco = houses.find('span', {'class': 'property-card__address'}).text.strip()
print(endereco)

area = houses.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
print(area + 'm²')

quartos = houses.find('li', {'class': 'property-card__detail-room'}).text.strip()
print(quartos)

wc = houses.find('li', {'class': 'property-card__detail-bathroom'}).text.strip()
print(wc)

vagas = houses.find('li', {'class': 'property-card__detail-garage'}).text.strip()
print(vagas)

valor = houses.find('div', {'class': 'property-card__price'}).text.strip()
print(valor)

condominio = houses.find('div', {'class': 'property-card__price-details--condo'}).text.strip()
print(condominio)

wlink = 'https://www.vivareal.com.br' + houses['href']
print(wlink)


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
