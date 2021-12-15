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
    print(
        f"{valor}{moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
    #print(f"{valor}{moeda[:3]} hoje custam {float(dolar[0]['bid']) * valor} {moeda[-3:]}") #necessario usar indices, porem apresentou erro

#%%
cotacao(20, 'USD-BRL')

#%%
cotacao(20, 'JPY-BRL')

#%%
try:
    cotacao(20, 'MIRO')
except:
    pass

#%%
try:
    cotacao(20, 'MIRO')
except Exception as error:
    print(error)
else:
    print('Ok')

#%%
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(
        f"{valor}{moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

#%%
    lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "ZEN-BRL",
        "JPY-BRL"
    ]

#%%
multi_moeda(20, "USD-BRL")

#%%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(
        f"{valor}{moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

#%%
multi_moeda(20, "USD-BRL")
multi_moeda(20, "EUR-BRL")
multi_moeda(20, "BTC-BRL")
multi_moeda(20, "ZEN-BRL")
multi_moeda(20, "JPY-BRL")

# %%
import backoff
import random

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries = 10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"

#%%
test_func()

#%%
test_func(42, 51, nome="miro")

# %%
import logging

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter (
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

#%%
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries = 10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f" RND: {rnd}")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"

#%%
test_func()

#%%
