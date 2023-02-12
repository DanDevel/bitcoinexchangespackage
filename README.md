# bitcoinexchangespackage
by Igor Azevedo

This is a Python 3.10 package.
Allows users to retreive BTC Bitcoin`s price up to 12 exchanges.

## PyPi Package:
https://pypi.org/project/bitcoinexchanges/

##Install command:
pip install bitcoinexchangespackage

## Available functions

### Retreive BTC price from Poloniex exchange:
poloniex_market(http)

## example:
polo_btc_price = poloniex_market(http)
print(polo_btc_price)

You will see the BTC Bitcoin price on Poloniex exchange.
if any error occurs it will return zero 0 (integer).


## All functions in the package:

1 - gemini_btcusd_market(http)
2 - cex_btcusd_market(http)
3 - bittrex_btcusd_market(http)
4 - kraken_btcusd_market(http)
5 - bitstamp_btcusd_market(http)
6 - blockchainluxemburgo_market(http)
7 - quadrigacx_market(http)
8 - braziliex_market(http)
9 - bitcambio_market(http)
10 - mercadobitcoin_market(http)
11 - okcoin_market(http)
12 - poloniex_market(http)





