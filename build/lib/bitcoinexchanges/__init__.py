import requests

MARKET_URLS = {
    "poloniex": "https://poloniex.com/public?command=returnTicker",
    "okcoin": "https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd",
    "mercadobitcoin": "https://www.mercadobitcoin.net/api/BTC/ticker/",
    "bitcambio": "https://bitcambio_api.blinktrade.com/api/v1/BRL/ticker",
    "braziliex": "https://braziliex.com/api/v1/public/ticker",
    "quadrigacx": "https://api.quadrigacx.com/v2/ticker?book=btc_usd",
    "blockchainluxemburgo": "https://blockchain.info/q/24hrprice",
    "bitstamp": "https://www.bitstamp.net/api/v2/ticker_hour/btcusd/",
    "kraken": "https://api.kraken.com/0/public/Ticker?pair=xbtusd",
    "bittrex": "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC",
    "cex": "https://cex.io/api/ticker/BTC/USD",
    "gemini": "https://api.gemini.com/v1/pubticker/btcusd"
}

def get_market_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['last']
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return 0

def get_btcusd_price():
    btcusd_prices = {}

    for market, url in MARKET_URLS.items():
        btcusd_price = get_market_price(url)
        btcusd_prices[market] = btcusd_price

    return btcusd_prices

btcusd_prices = get_btcusd_price()
for market, price in btcusd_prices.items():
    print(f"{market}: {price}")
