#!/usr/bin/python
#Python 2.7 framework for Tradesatoshi's public and private API
#    for use in the development of trading robots
import time
import hmac
import urllib
import requests
import hashlib
import base64
import sys
import json

#for manually entering your keys, uncomment
# API_KEY = '<YOUR PUBLIC API KEY>'
# API_SECRET = '<YOUR PRIVATE API KEY - NEVER SHARE>'

#prompting user for keys
API_KEY = str(raw_input("\nAPI KEY? : "))
API_SECRET = str(raw_input("API SECRET? : "))


def api_query( method, req = None ):
    if not req:
        req = {}
    #print "def api_query( method = " + method + ", req = " + str( req ) + " ):"
    time.sleep( 1 )
    public_set = set([ "GetCurrencies","GetTicker?","GetMarketHistory?","GetMarketSummary?","GetMarketSummaries","GetOrderBook?" ])
    private_set = set([ "GetBalance","GetBalances","GetOrder","GetOrders","SubmitOrder","CancelOrder","GetTradeHistory","GenerateAddress","SubmitWithdraw","GetDeposits","GetWithdrawals" ])
    if method in public_set:
        url = "https://tradesatoshi.com/api/public/" + method
        if req:
            for param in req:
                url += str( param )
        print 'url:',url
        r = requests.get( url )
    elif method in private_set:
        url = "https://tradesatoshi.com/api/private/" + method
        nonce = str( int( time.time() ) )
        post_data = json.dumps( req );
        requestContentBase64String = base64.b64encode(post_data)
        signature = API_KEY + "POST" + urllib.quote_plus( url ).lower() + nonce + requestContentBase64String
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode( API_SECRET ), signature, hashlib.sha512).digest())
        header_value = "Basic " + API_KEY + ":" + hmacsignature + ":" + nonce
        headers = { 'Authorization': header_value, 'Content-Type':'application/json; charset=utf-8' }
        print 'url:',url
        r = requests.post( url, data = post_data, headers = headers )
    
    response = r.text
    print "( Response ): " + response
    return response.replace("false","False").replace("true","True").replace('":null','":None' )



def getCurrencies():
    try:
        return api_query("GetCurrencies")
    except: 
        print 'problem in getCurrencies'
        return None
# test - GOOD
# print "GetCurrencies: ",getCurrencies()
# GetCurrencies:  {u'message': None, u'result': [{u'status': u'OK', u'currency': u'100', u'currencyLong': u'100coin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'1337', u'currencyLong': u'1337', u'minConfirmation': 12, u'txFee': 5.0}, {u'status': u'OK', u'currency': u'42', u'currencyLong': u'42', u'minConfirmation': 12, u'txFee': 2e-08}, {u'status': u'OK', u'currency': u'420G', u'currencyLong': u'GanjaCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'4CHN', u'currencyLong': u'ChanCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'611', u'currencyLong': u'SixEleven', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'808', u'currencyLong': u'808', u'minConfirmation': 6, u'txFee': 0.01}, {u'status': u'Maintenance', u'currency': u'8BIT', u'currencyLong': u'8Bit', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ABJ', u'currencyLong': u'Abjcoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'Offline', u'currency': u'ABJo', u'currencyLong': u'Abjcoinold', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ACC', u'currencyLong': u'Acchain', u'minConfirmation': 10, u'txFee': 0.2}, {u'status': u'OK', u'currency': u'ADBT', u'currencyLong': u'ADDBIT', u'minConfirmation': 24, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'AI', u'currencyLong': u'Artificial Intellegence', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'AM', u'currencyLong': u'AeroMe', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'AMY', u'currencyLong': u'Amygws', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'AREPA', u'currencyLong': u'Arepacoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'ASL', u'currencyLong': u'Astral', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'ASPIR', u'currencyLong': u'Aspirecoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ATOM', u'currencyLong': u'AtomicCoin', u'minConfirmation': 6, u'txFee': 0.0004}, {u'status': u'OK', u'currency': u'BCC', u'currencyLong': u'Bitconnect', u'minConfirmation': 18, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'BCH', u'currencyLong': u'Bitcoin Cash', u'minConfirmation': 6, u'txFee': 1e-05}, {u'status': u'OK', u'currency': u'BCS', u'currencyLong': u'BitcoinStake', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BELA', u'currencyLong': u'BellaCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BETC', u'currencyLong': u'Betcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BLK', u'currencyLong': u'Blackcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BOAT', u'currencyLong': u'Doubloon ', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BOG', u'currencyLong': u'Bogcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BOLI', u'currencyLong': u'Bolivarcoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'BP', u'currencyLong': u'Bitpaycoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BRM', u'currencyLong': u'BitRaam', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'Offline', u'currency': u'BRO', u'currencyLong': u'Bitradio', u'minConfirmation': 4, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'BSD', u'currencyLong': u'BitSend ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'BTA', u'currencyLong': u'BATA', u'minConfirmation': 50, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'BTC', u'currencyLong': u'Bitcoin', u'minConfirmation': 6, u'txFee': 0.002}, {u'status': u'OK', u'currency': u'BTCD', u'currencyLong': u'Bitcoindark', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'BTCG', u'currencyLong': u'BitcoinGo', u'minConfirmation': 30, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'BTCGS', u'currencyLong': u'BitcoinGoScrypt', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BTCR', u'currencyLong': u'BtcRuble', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BTCZ', u'currencyLong': u'BitcoinZ', u'minConfirmation': 7, u'txFee': 0.3}, {u'status': u'OK', u'currency': u'BTG', u'currencyLong': u'BitcoinGold', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'BTM', u'currencyLong': u'Bitmark', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BTX', u'currencyLong': u'BitCore', u'minConfirmation': 6, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BUMBA', u'currencyLong': u'Bumbacoin', u'minConfirmation': 6, u'txFee': 0.0004}, {u'status': u'OK', u'currency': u'BUN', u'currencyLong': u'BunnyCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BUY', u'currencyLong': u'Buycoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'BUZZ', u'currencyLong': u'BUZZcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CAP', u'currencyLong': u'Bottlecaps', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CBX', u'currencyLong': u'CryptoBullion', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'CCC', u'currencyLong': u'Chococoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'CDN', u'currencyLong': u'Canada eCoin', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CHEE', u'currencyLong': u'Cheese Coin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CLAM', u'currencyLong': u'Clam', u'minConfirmation': 12, u'txFee': 0.0005}, {u'status': u'OK', u'currency': u'CLOAK', u'currencyLong': u'CloakCoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'COLX', u'currencyLong': u'ColossusCoinXT', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CPC', u'currencyLong': u'Capricoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CRBIT', u'currencyLong': u'Creditbit', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'CURE', u'currencyLong': u'Curecoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'CYC', u'currencyLong': u'Conspiracycoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'DASH', u'currencyLong': u'Dash', u'minConfirmation': 12, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'DBTC', u'currencyLong': u'Debitcoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'DEM', u'currencyLong': u'Deutsche eMark', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'DGB', u'currencyLong': u'DigiByte', u'minConfirmation': 12, u'txFee': 1e-05}, {u'status': u'OK', u'currency': u'DGMS', u'currencyLong': u'Digigems', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'DIEM', u'currencyLong': u'Carpe Diem Coins', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'DLR', u'currencyLong': u'DOLLAROnline', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'DNR', u'currencyLong': u'Denarius', u'minConfirmation': 12, u'txFee': 1e-06}, {u'status': u'OK', u'currency': u'DOGE', u'currencyLong': u'Dogecoin', u'minConfirmation': 10, u'txFee': 1.0}, {u'status': u'OK', u'currency': u'DOT', u'currencyLong': u'Dotcoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'Offline', u'currency': u'DWC', u'currencyLong': u'DeepWebCash', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'EBC', u'currencyLong': u'Ebookcoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'EMC2', u'currencyLong': u'Einsteinium ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ENT', u'currencyLong': u'Eternity', u'minConfirmation': 6, u'txFee': 0.0002}, {u'status': u'Maintenance', u'currency': u'ESP2', u'currencyLong': u'Espers', u'minConfirmation': 6, u'txFee': 0.0002}, {u'status': u'OK', u'currency': u'EVIL', u'currencyLong': u'EvilCoin', u'minConfirmation': 26, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'FLAP', u'currencyLong': u'FlappyCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'FLO', u'currencyLong': u'FlorinCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'GAME', u'currencyLong': u'GameCredits ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'GB', u'currencyLong': u'GoldBlocks', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'GLD', u'currencyLong': u'GoldCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'GNC', u'currencyLong': u'Generationchanger', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'GPK', u'currencyLong': u'Gopnik Coin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'GRS', u'currencyLong': u'Groestlcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'HALLO', u'currencyLong': u'HalloweenCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'HSR', u'currencyLong': u'Hshare', u'minConfirmation': 12, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'HTML5', u'currencyLong': u'HTMLCOIN', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'HUE', u'currencyLong': u'Dilmacoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'HUSH', u'currencyLong': u'HUSH', u'minConfirmation': 10, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'HYPER', u'currencyLong': u'Hyper', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'IMS', u'currencyLong': u'Ind Money system', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'INSN', u'currencyLong': u'InsaneCoin', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'J', u'currencyLong': u'Joincoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'JESUS', u'currencyLong': u'JesusCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'KASH', u'currencyLong': u'Kashcoin', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'KMD', u'currencyLong': u'Komodo', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'KNLX', u'currencyLong': u'Knolix', u'minConfirmation': 18, u'txFee': 0.0}, {u'status': u'OK', u'currency': u'KNX', u'currencyLong': u'KNOXCOIN', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'KORE', u'currencyLong': u'KoreCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'KURT', u'currencyLong': u'Kurrent ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'KZC', u'currencyLong': u'Kzcash', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'LBC', u'currencyLong': u'LBRY Credits', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'LDOGE', u'currencyLong': u'LiteDoge', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'LTC', u'currencyLong': u'Litecoin', u'minConfirmation': 6, u'txFee': 0.02}, {u'status': u'OK', u'currency': u'LTK', u'currencyLong': u'Litkoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MAGA', u'currencyLong': u'Magacoin', u'minConfirmation': 12, u'txFee': 0.0}, {u'status': u'OK', u'currency': u'MAXT', u'currencyLong': u'Maxtime', u'minConfirmation': 30, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MBCH', u'currencyLong': u'MillionBitcoinCash', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MDC', u'currencyLong': u'Madcoin', u'minConfirmation': 50, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MGC', u'currencyLong': u'MergeCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MGT', u'currencyLong': u'MAGNATUM', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MNC', u'currencyLong': u'MinCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'MONA', u'currencyLong': u'Monacoin', u'minConfirmation': 12, u'txFee': 0.02}, {u'status': u'OK', u'currency': u'NDC', u'currencyLong': u'NeedleCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'NET', u'currencyLong': u'NetCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'NEVA', u'currencyLong': u'Nevacoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'NKA', u'currencyLong': u'Incakoin', u'minConfirmation': 6, u'txFee': 0.0005}, {u'status': u'OK', u'currency': u'NOBT', u'currencyLong': u'Nobtcoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'NVC', u'currencyLong': u'Novacoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'NXS', u'currencyLong': u'Nexus ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'NYAN', u'currencyLong': u'NyanCoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'OBC', u'currencyLong': u'ObamaCare', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'OHM', u'currencyLong': u'Ohm', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'OK', u'currencyLong': u'Okcash', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ONX', u'currencyLong': u'ONIX', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ORB', u'currencyLong': u'Orbitcoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PAC', u'currencyLong': u'Paccoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PAK', u'currencyLong': u'Pakcoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'Offline', u'currency': u'PIE', u'currencyLong': u'Piecoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PIGGY', u'currencyLong': u'Piggycoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'PINK', u'currencyLong': u'Pinkcoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'PIP', u'currencyLong': u'PipCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'POSW', u'currencyLong': u'PoSW Coin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'POT', u'currencyLong': u'PotCoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PPC', u'currencyLong': u'Peercoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'PRUX', u'currencyLong': u'Prux', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PRX', u'currencyLong': u'Printerium', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PTC', u'currencyLong': u'Pesetacoin', u'minConfirmation': 6, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'PUT', u'currencyLong': u'PutinCoin2', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'QTL', u'currencyLong': u'Quatloo ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'QTM', u'currencyLong': u'Quantum', u'minConfirmation': 10, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'RC', u'currencyLong': u'RussiaCoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'RDD', u'currencyLong': u'Reddcoin', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'RGC', u'currencyLong': u'RGCoin ', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'RIO', u'currencyLong': u'Riocoin', u'minConfirmation': 18, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'RIOC', u'currencyLong': u'Rio Coin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'RUP', u'currencyLong': u'Ruppe', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'RUPX', u'currencyLong': u'RupayaCoin', u'minConfirmation': 25, u'txFee': 0.1}, {u'status': u'Offline', u'currency': u'RUPXo', u'currencyLong': u'RupayaCoinold', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SAND', u'currencyLong': u'Beachcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SAT2', u'currencyLong': u'Saturn2Coin', u'minConfirmation': 18, u'txFee': 0.0}, {u'status': u'OK', u'currency': u'SCF', u'currencyLong': u'MinuteCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SCOBY', u'currencyLong': u'ScoobyCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'SDC', u'currencyLong': u'ShadowCash', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'SHA', u'currencyLong': u'Shacoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'SHND', u'currencyLong': u'Stronghands', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SIB', u'currencyLong': u'Sibcoin', u'minConfirmation': 6, u'txFee': 0.0004}, {u'status': u'OK', u'currency': u'SLC', u'currencyLong': u'SocialCoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'SLOTH', u'currencyLong': u'Slothcoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SOJ', u'currencyLong': u'Sojourn', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'SOLAR', u'currencyLong': u'Solar', u'minConfirmation': 24, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'START', u'currencyLong': u'Startcoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'STAX', u'currencyLong': u'Staxcoin2', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'STRAT', u'currencyLong': u'STRATIS', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'SYNC', u'currencyLong': u'SYNC', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'TAJ', u'currencyLong': u'TajCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'TATO', u'currencyLong': u'Tattoocoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'TEA', u'currencyLong': u'TeaCoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'TMRW', u'currencyLong': u'TomorrowCoin ', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'TPAY', u'currencyLong': u'TrollPlay', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'TRC', u'currencyLong': u'Terracoin', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'TRK', u'currencyLong': u'Truckcoin', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'TRUMP', u'currencyLong': u'Trumpcoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'UNO', u'currencyLong': u'Unobtanium ', u'minConfirmation': 12, u'txFee': 0.0002}, {u'status': u'Offline', u'currency': u'USD', u'currencyLong': u'USD', u'minConfirmation': 0, u'txFee': 7.0}, {u'status': u'OK', u'currency': u'VCC', u'currencyLong': u'Vclassiccoin', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'VCCO', u'currencyLong': u'Vadercorpcoin', u'minConfirmation': 6, u'txFee': 0.001}, {u'status': u'OK', u'currency': u'VLTC', u'currencyLong': u'Vault Coin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'VOT', u'currencyLong': u'VoteCoin', u'minConfirmation': 25, u'txFee': 0.3}, {u'status': u'OK', u'currency': u'VPN', u'currencyLong': u'VPNCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'Maintenance', u'currency': u'VRC', u'currencyLong': u'VeriCoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'VSX', u'currencyLong': u'Vsync ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'VTA', u'currencyLong': u'Virtacoin', u'minConfirmation': 16, u'txFee': 0.0}, {u'status': u'OK', u'currency': u'WDC', u'currencyLong': u'WorldCoin ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'WJK', u'currencyLong': u'WojakCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'WOMEN', u'currencyLong': u'WomenCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'WORM', u'currencyLong': u'HealthyWormCoin ', u'minConfirmation': 12, u'txFee': 1e-05}, {u'status': u'OK', u'currency': u'WW', u'currencyLong': u'WayaWolfCoin', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'WWC', u'currencyLong': u'Wounded Warrior Coin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XBC', u'currencyLong': u'Bitcoin Plus', u'minConfirmation': 16, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'XBY', u'currencyLong': u'XtraBYtes', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XCRE', u'currencyLong': u'Creatio', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'XHI', u'currencyLong': u'Hicoin', u'minConfirmation': 10, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'XMG', u'currencyLong': u'Magi', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XMY', u'currencyLong': u'Myriad ', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XP', u'currencyLong': u'ExperiencePoints', u'minConfirmation': 6, u'txFee': 1000.0}, {u'status': u'OK', u'currency': u'XSH', u'currencyLong': u'Shield', u'minConfirmation': 18, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XSPEC', u'currencyLong': u'spectrecoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'XVG', u'currencyLong': u'Verge', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'XVP', u'currencyLong': u'VirtacoinPlus', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'XWC', u'currencyLong': u'WhiteCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'YASH', u'currencyLong': u'YashCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'YES', u'currencyLong': u'YesCoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'YOC', u'currencyLong': u'YOCOIN', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'YOVI', u'currencyLong': u'Yovi', u'minConfirmation': 10, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'YUANC', u'currencyLong': u'Yuancoin', u'minConfirmation': 16, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ZBC', u'currencyLong': u'Zilbercoin', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ZCL', u'currencyLong': u'Zclassic', u'minConfirmation': 6, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'ZEC', u'currencyLong': u'Zcash', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'ZEIT', u'currencyLong': u'Zeitcoin', u'minConfirmation': 12, u'txFee': 0.01}, {u'status': u'OK', u'currency': u'ZEN', u'currencyLong': u'Zencash', u'minConfirmation': 6, u'txFee': 0.0001}, {u'status': u'OK', u'currency': u'ZER', u'currencyLong': u'ZERO', u'minConfirmation': 12, u'txFee': 0.1}, {u'status': u'OK', u'currency': u'ZYD', u'currencyLong': u'ZayedCoin ', u'minConfirmation': 6, u'txFee': 0.0001}], u'success': True}


#PUBLIC

def getTicker(market):
    try:
        return api_query("GetTicker?",["market="+market])
    except:
        return None
# test - GOOD
# print "getTicker(DOT_BTC): ",getTicker('DOT_BTC')
# getTicker(DOT_BTC):  {u'message': None, u'result': {u'ask': 7e-07, u'bid': 1e-07, u'last': 6e-07, u'market': u'DOT_BTC'}, u'success': True}

        
def getMarketHistory(market,count=''):
    try:
        if count is not '': return api_query("GetMarketHistory?",["market="+market,"&count="+count])
        else: return api_query("GetMarketHistory?",["market="+market])
    except:
        return None
# test - GOOD
# print "getMarketHistory(DOT_BTC,1): ",getMarketHistory('DOT_BTC','1')
# print "getMarketHistory(DOT_BTC) <20 is default>: ",getMarketHistory('DOT_BTC')
# getMarketHistory(DOT_BTC,1):  {u'message': None, u'result': [{u'timeStamp': u'2017-11-15T09:03:42.19', u'price': 6e-07, u'orderType': u'Buy', u'total': 6e-06, u'id': 1415261, u'quantity': 10.0}], u'success': True}
# getMarketHistory(DOT_BTC) <20 is default>:  {u'message': None, u'result': [{u'timeStamp': u'2017-11-15T09:03:42.19', u'price': 6e-07, u'orderType': u'Buy', u'total': 6e-06, u'id': 1415261, u'quantity': 10.0}, {u'timeStamp': u'2017-11-14T18:58:15.093', u'price': 6.4e-07, u'orderType': u'Buy', u'total': 1.37e-05, u'id': 1410786, u'quantity': 21.40616875}, {u'timeStamp': u'2017-11-13T06:57:31.627', u'price': 3e-07, u'orderType': u'Buy', u'total': 3e-05, u'id': 1397301, u'quantity': 100.0}, {u'timeStamp': u'2017-11-13T06:49:14.477', u'price': 8.5e-07, u'orderType': u'Buy', u'total': 0.00025542, u'id': 1397279, u'quantity': 300.49977354}, {u'timeStamp': u'2017-11-13T06:48:52.29', u'price': 7.4e-07, u'orderType': u'Buy', u'total': 0.00094272, u'id': 1397276, u'quantity': 1273.94868047}, {u'timeStamp': u'2017-11-13T06:48:36.803', u'price': 7e-07, u'orderType': u'Buy', u'total': 0.02105633, u'id': 1397272, u'quantity': 30080.47442857}, {u'timeStamp': u'2017-11-13T06:48:36.787', u'price': 6.9e-07, u'orderType': u'Buy', u'total': 0.00087025, u'id': 1397271, u'quantity': 1261.22528986}, {u'timeStamp': u'2017-11-13T06:48:36.787', u'price': 6.5e-07, u'orderType': u'Buy', u'total': 0.00016408, u'id': 1397270, u'quantity': 252.42324716}, {u'timeStamp': u'2017-11-13T06:48:36.773', u'price': 5.5e-07, u'orderType': u'Buy', u'total': 0.000517, u'id': 1397269, u'quantity': 940.0}, {u'timeStamp': u'2017-11-13T06:48:36.757', u'price': 5e-07, u'orderType': u'Buy', u'total': 4.985e-05, u'id': 1397268, u'quantity': 99.69999999}, {u'timeStamp': u'2017-11-13T06:48:36.74', u'price': 4.9e-07, u'orderType': u'Buy', u'total': 0.00030577, u'id': 1397267, u'quantity': 624.01408696}, {u'timeStamp': u'2017-11-13T06:48:36.723', u'price': 4e-07, u'orderType': u'Buy', u'total': 0.00068486, u'id': 1397266, u'quantity': 1712.15136363}, {u'timeStamp': u'2017-11-12T19:55:19.257', u'price': 3.5e-07, u'orderType': u'Sell', u'total': 0.000224, u'id': 1393067, u'quantity': 640.0}, {u'timeStamp': u'2017-11-12T18:46:22.93', u'price': 5e-07, u'orderType': u'Buy', u'total': 0.00032, u'id': 1392638, u'quantity': 640.0}, {u'timeStamp': u'2017-11-12T12:07:31.043', u'price': 6e-07, u'orderType': u'Buy', u'total': 0.00015103, u'id': 1390261, u'quantity': 251.71324018}, {u'timeStamp': u'2017-11-12T09:56:43.303', u'price': 7.4e-07, u'orderType': u'Buy', u'total': 0.01186817, u'id': 1389590, u'quantity': 16038.06300171}, {u'timeStamp': u'2017-11-12T09:56:43.303', u'price': 7.4e-07, u'orderType': u'Buy', u'total': 0.00232769, u'id': 1389589, u'quantity': 3145.53211092}, {u'timeStamp': u'2017-11-12T09:56:32.8', u'price': 6.9e-07, u'orderType': u'Buy', u'total': 0.00223263, u'id': 1389588, u'quantity': 3235.68885145}, {u'timeStamp': u'2017-11-12T09:56:32.8', u'price': 6.7e-07, u'orderType': u'Buy', u'total': 6.772e-05, u'id': 1389587, u'quantity': 101.07943884}, {u'timeStamp': u'2017-11-12T09:56:32.8', u'price': 6.5e-07, u'orderType': u'Buy', u'total': 0.00082306, u'id': 1389586, u'quantity': 1266.24719719}], u'success': True}

     
def getMarketSummary(market):
    try:
        return api_query("GetMarketSummary?",["market="+market])
    except:
        return None
# test - GOOD
# print "getMarketSummary(DOT_BTC): ",getMarketSummary('DOT_BTC')
# getMarketSummary(DOT_BTC):  {u'message': None, u'result': {u'volume': 0.0, u'last': 6e-07, u'openSellOrders': 30, u'bid': 1e-07, u'openBuyOrders': 2, u'high': 0.0, u'low': 0.0, u'ask': 7e-07, u'change': -6.25, u'market': u'DOT_BTC', u'baseVolume': 0.0}, u'success': True}

 
def getMarketSummaries():
    try:
        return api_query("GetMarketSummaries")
    except:
        return None
#test - GOOD
# print "getMarketSummaries(): ",getMarketSummaries()

def getOrderBook(market,t='both',depth=20):
    try:
        return api_query("GetOrderBook?",['market='+market,'&type='+t,'&depth='+depth])
    except:
        return None
# test - GOOD
# print "getOrderBook(DOT_BTC,both,20): ",getOrderBook('DOT_BTC','both','20')
# getOrderBook(DOT_BTC,both,20):  {u'message': None, u'result': {u'sell': [{u'rate': 7e-07, u'quantity': 36544.43687017}, {u'rate': 8.9e-07, u'quantity': 2061.22561945}, {u'rate': 1e-06, u'quantity': 79.94312643}, {u'rate': 1.16e-06, u'quantity': 115.86727534}, {u'rate': 2.22e-06, u'quantity': 75.31232828}, {u'rate': 2.36e-06, u'quantity': 826.81122015}, {u'rate': 5.9e-06, u'quantity': 38.0}, {u'rate': 6e-06, u'quantity': 39.65818933}, {u'rate': 8.3e-06, u'quantity': 30.0}, {u'rate': 8.88e-06, u'quantity': 1000.0}, {u'rate': 9.99e-06, u'quantity': 2.0}, {u'rate': 1.234e-05, u'quantity': 450.0}, {u'rate': 1.5e-05, u'quantity': 2792.91222221}, {u'rate': 2.547e-05, u'quantity': 2.0}, {u'rate': 9.99e-05, u'quantity': 2.0}, {u'rate': 0.0002547, u'quantity': 2.0}, {u'rate': 0.0006528, u'quantity': 2.0}, {u'rate': 0.000999, u'quantity': 2.0}, {u'rate': 0.00099999, u'quantity': 0.07000049}, {u'rate': 0.002547, u'quantity': 2.0}], u'buy': [{u'rate': 1e-07, u'quantity': 1000.0}, {u'rate': 1e-07, u'quantity': 17349.07215215}]}, u'success': True}

#PRIVATE
  
def getBalance(currency):
    try:
        return api_query("GetBalance", {'Currency':'BTC'} )
    except:
        return None
# test - GOOD
# print "getBalance(BTC): ",getBalance('BTC')
 
 
def getBalances():
    try:
        return api_query("GetBalances")
    except:
           
        return None
# test - GOOD
# print "getBalances(): ",getBalances()
    
def getOrder(orderid):
    try:
        return api_query("GetOrder",{"OrderId":orderid})
    except:
          
        return None
# test: GOOD
# print "getOrder(7404747):",getOrder(7404747)
# result: {"success":True,"message":None,"result":{"id":7404747,"market":"BOLI_BTC","type":"Buy","amount":500.00000000,"rate":0.00000001,"remaining":500.00000000,"total":0.00000500,"status":"Pending","timestamp":"2017-12-05T20:43:23.157","isApi":False}}
     
def getOrders(market,count):
    try:
        return api_query("GetOrders",{"Market":market,"Count":count})
    except:
         
        return None
# test - GOOD
# print "getOrders(BOLI_BTC,1): ",getOrders("BOLI_BTC",1)
# print "getOrders(BOLI_BTC,2): ",getOrders("BOLI_BTC",2) 
     
def submitOrder(market,typ,amount,price):
    try:
        return api_query("SubmitOrder",{"Market":market,"Type":typ,"Amount":amount,"Price":price})
    except:
        return None
# test: GOOD
# print "submitOrder(BTG_BTC,buy,500,0.00000001)",submitOrder("BTG_BTC","Buy",500,0.00000001)
# result: {"success":True,"message":None,"result":{"orderId":7404912,"filled":[]}}
     
def cancelOrder(typ,orderid,market):
    try:
        return api_query("CancelOrder",{"Type":typ,"OrderId":orderid,"Market":market})
    except:
        return None
# test: GOOD
# print "cancelOrder(buy,7404747,BOLI_BTC):",cancelOrder("Buy",7404747,"BOLI_BTC")
# result: {"success":True,"message":None,"result":{"canceledOrders":[7404747]}}
     
def getTradeHistory(market,count):
    try:
        return api_query("GetTradeHistory",{"Market":market,"Count":count})
    except:
        return None
# test: GOOD
# print "getTradeHistory(DOGE_BTC,20)<--default is 20: ",getTradeHistory("DOGE_BTC",20)
# result: {"success":True,"message":None,"result":[{"id":1635972,"market":"DOGE_BTC","type":"Buy","amount":25.00000000,"rate":0.00000022,"fee":0.00000001,"total":0.00000549,"timestamp":"2017-12-05T21:05:10.933","isApi":False},{"id":1635976,"market":"DOGE_BTC","type":"Sell","amount":25.00000000,"rate":0.00000021,"fee":0.00000001,"total":0.00000524,"timestamp":"2017-12-05T21:05:28.043","isApi":False}]}
# note:  isApi = false here, however the buy and sell trades on DOGE/BTC were made with the api calls. could be a server bug
     
def generateAddress(currency):
    try:
        return api_query("GenerateAddress",{"Currency":currency})
    except:         
        return None
# test: GOOD
# print "generateAddress(BTG): ",generateAddress("BTG")
# result: {"success":True,"message":None,"result":{"currency":"BTG","address":"GeYuunhKMG2n9phY4NmxExfEpxFUs2KHSW"}}
     
def submitWithdraw(currency,address,amount):
    try:
        return api_query("SubmitWithdraw",{"Currency":currency,"Address":address,"Amount":amount})
    except:
        return None
# test: GOOD              coinbase address                  should send 0.01
# print "submitWithdraw(BTC,14eAisDycLsNoHY5ojMwkTaAJHuW6PvR2e,0.012):",submitWithdraw("BTC","14eAisDycLsNoHY5ojMwkTaAJHuW6PvR2e", 0.012)
# result: {"success":true,"message":null,"result":{"withdrawalId":47959}}
# note: after checking balances in tradesatoshi.com this is in a state of "pending withdraw"
#       after several minutes the withdrawal finished and is now pending in coinbase, yay!
     
def getDeposits(currency,count):
    try:
        return api_query("GetDeposits",{"Currency":currency,"Count":count})
    except:
        return None
# # test: GOOD
# print "getDeposits(BOLI):",getDeposits("BOLI",20)
# result: {"success":True,"message":None,"result":[{"id":836404,"currency":"BOLI","currencyLong":"Bolivarcoin","amount":49.99990000,"status":"UnConfirmed","txid":"62954f1d6e86ddd4c5384801628de82877d1c1a7c98d29d1b0be9c0526211f6c","confirmations":0,"timeStamp":"2017-12-05T21:39:59"}]}
# note:  the transfer of BOLI from Cryptopia to Tradesatoshi took about 20 minutes
     
def getWithdrawals(currency,count):
    try:
        return api_query("GetWithdrawals", {"Currency":currency,"Count":count})
    except:         
        return None
# test: GOOD
# print "getWithdrawals(BTC,20):",getWithdrawals("BTC",20)
# result: {"success":True,"message":None,"result":[{"id":47959,"currency":"BTC","currencyLong":"Bitcoin","amount":0.01200000,"fee":0.00200000,"address":"14eAisDycLsNoHY5ojMwkTaAJHuW6PvR2e","status":"Complete","txid":"72360e800a9cf2a528c8c14597ae8e737ec70ac5c5cb2b4e9347943acb7e3cdc","confirmations":0,"timeStamp":"2017-12-05T21:28:12.023","isApi":True}]}

