
import urllib3
import json
import certifi

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

def poloniex_market(http):
    try:
        url = "https://poloniex.com/public?command=returnTicker"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['USDT_BTC']['last']
        return last_btc        
    except Exception as err:
        return 0

def okcoin_market(http):
    try:
        url = "https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['ticker']['last']
        return last_btc        
    except Exception as err:
        return 0

def mercadobitcoin_market(http):
    try:
        url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['ticker']['last']
        return last_btc
    except Exception as err:
        return 0

def bitcambio_market(http):
    try:
        url = "https://bitcambio_api.blinktrade.com/api/v1/BRL/ticker"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0

def braziliex_market(http):
    try:        
        url = "https://braziliex.com/api/v1/public/ticker"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['btc_brl']['last']
        return last_btc
    except Exception as err:
        return 0

def quadrigacx_market(http):
    try:    
        url = "https://api.quadrigacx.com/v2/ticker?book=btc_usd"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0

def blockchainluxemburgo_market(http):
    try:
        url = "https://blockchain.info/q/24hrprice"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData
        return last_btc
    except Exception as err:
        return 0
    
def bitstamp_btcusd_market(http):
    try:    
        url = "https://www.bitstamp.net/api/v2/ticker_hour/btcusd/"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0
    
def kraken_btcusd_market(http):
    try:
        url = "https://api.kraken.com/0/public/Ticker?pair=xbtusd"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0
    
def bittrex_btcusd_market(http):
    try:     
        url = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['result']['Last'] 
        return last_btc
    except Exception as err:
        return 0

def cex_btcusd_market(http):
    try:    
        url = "https://cex.io/api/ticker/BTC/USD"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0

def gemini_btcusd_market(http):
    try:
        url = "https://api.gemini.com/v1/pubticker/btcusd"
        r = http.request('GET', url)
        myData = json.loads(r.data.decode('utf-8'))
        last_btc = myData['last']
        return last_btc
    except Exception as err:
        return 0
