############################################################################################################################
# # ATIVAR AMBIENTE #
# "C:\Users\altamiro.sousa\OneDrive\PARTICULAR\Cursos\Bootcampo - Eng.Dados\A003-Fundamentos_de_Ingestão_de_Dados\.venv\Scripts\activate.bat"
# ipython
############################################################################################################################


#%%
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
qtd_imoveis = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.',''))

#%%
len(houses)

#%%
qtd_imoveis

#%%
