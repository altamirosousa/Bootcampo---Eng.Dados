#%%
# imports
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
#url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL' #usado endereço errado
ret = requests.get(url)

#%%
if ret:
    print(ret)
else:
    print('Falhou')

#%%
dolar = json.loads(ret.text) ['USDBRL']
#dolar = json.loads(ret.text) [0],['USDBRL'] #necessario fazer indice

#%%
dolar

#%%
dolar['bid']
#dolar[0]['bid'] #necessario fazer indice

#%%
print( f" 20 Dólares hoje custam {float(dolar['bid']) * 20} reais")
#print( f" 20 Dólares hoje custam {float(dolar[0]['bid']) * 20} reais") #necessario usar indices, porem apresentou erro

#%%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    #url = 'https://economia.awesomeapi.com.br/last/{}'.format(moeda)
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor}{moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
    #print(f"{valor}{moeda[:3]} hoje custam {float(dolar[0]['bid']) * valor} {moeda[-3:]}") #necessario usar indices, porem apresentou erro

#%%
cotacao(20, 'USD-BRL')

#%%
