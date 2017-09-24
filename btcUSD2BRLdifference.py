import json
import urllib2

urlBTCUSD = 'https://www.bitstamp.net/api/ticker/'
urlBRL = 'http://api.fixer.io/latest?base=USD'
urlMercado = 'https://www.mercadobitcoin.net/api/BTC/ticker/'
urlFOXBIT = 'https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC'

json_obj_BTCUSD = urllib2.urlopen(urlBTCUSD)
json_obj_BRL = urllib2.urlopen(urlBRL)
json_obj_Mercado = urllib2.urlopen(urlMercado)
json_obj_FOXBIT = urllib2.urlopen(urlFOXBIT)

btc = json.load(json_obj_BTCUSD)
brl = json.load(json_obj_BRL)
mb = json.load(json_obj_Mercado)
fb = json.load(json_obj_FOXBIT)

btcUSDPrice = float(btc['last'])
usdBRL = float(brl['rates']['BRL'])
mercadob = float(mb['ticker']['last'])
foxbit = float(fb['last'])

btcUSD2BRL = btcUSDPrice * usdBRL

btcBRLAverage = (mercadob + foxbit) / 2  

difference = (abs(btcBRLAverage - btcUSD2BRL)) / btcBRLAverage * 100.0

print('%.2f' %btcBRLAverage)
print('%.2f' %btcUSD2BRL)
print('%.2f' %difference)
