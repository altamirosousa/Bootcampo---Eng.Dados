#%%
# imports
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL'
ret = requests.get(url)

#%%
if ret:
    print(ret)
else:
    print('Falhou')

#%%
dolar = json.loads(ret.text)

#%%
dolar

#%%
dolar[0]['bid']

#%%
print( f" 20 Dólares hoje custam {float(dolar[0]['bid']) * 20} reais")

#%%
#### Plus Altamiro- Informar valor a ser convertido ####
valor = float(input(" qual o valor a ser convertido? R$"))
print ("U${:.2f} na cotação atual (R${:.2}), equivale a R${:.2f}".format(valor, (float(dolar[0]['bid'])), ((float(dolar[0]['bid']) * valor))))

#%%
