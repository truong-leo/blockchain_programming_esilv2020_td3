import requests
import json
import sqlite3

"""
currencies = requests.get('https://api.pro.coinbase.com/currencies')

print(currencies.status_code)

currencies_json = json.loads(currencies.text)

for i in currencies_json:
    print("%s : %s" % (i['id'], i['name']))
"""


def getAvailableCryptocurrencies():
    products = requests.get('https://api.pro.coinbase.com/products')

    print(products.status_code)

    products_json = json.loads(products.text)

    available_cryptocurrencies = 40 * [0]

    print(available_cryptocurrencies[39])
    print(len(available_cryptocurrencies))
    i = 0
    deja_present = True

    for e in products_json:

        for j in range(0, 40):
            if (e['base_currency'] != available_cryptocurrencies[i]):
                deja_present = False

        if (deja_present == False):
            available_cryptocurrencies[i] = e['base_currency']
            print(e['base_currency'])
            i = i + 1

        deja_present = True

def getDepth(direction='ask', pair = 'BTCUSD'):
    adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/book'

    priceof = direction
    direction = direction + 's'
    data = requests.get(adress)
    data_json = json.loads(data.text)



    for e in data_json[direction]:
        print('The price of the ' + priceof + ' for ' + pair + ' is : ' + e[0])

def getOrderBook(direction='askorbid', pair = 'BTCUSD'):
    adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/book?level=2'

    priceof = direction
    direction = direction + 's'
    data = requests.get(adress)
    data_json = json.loads(data.text)

    print("The first 50 values of the " + priceof + " order book are : " + "\n")

    print('%7s | %12s | %10s' % ('PRICE ','SIZE   ','NUM-ORDERS'))
    print(35 * '_')
    for e in data_json[direction]:
        print('%7s | %12s | %5d' % (e[0],e[1],e[2]))

def refreshDataCandlee(pair = 'BTCUSB', duration = '5m'):
    adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/candles'

    data = requests.get(adress)
    data_json = json.loads(data.text)

    numberofminutes = int(duration[0:(len(duration)-1)])

    #ime, low, high, open, clone, volume

    time = '?????'

    low = (data_json[0])[1]
    for i in range(numberofminutes-1):
        if(data_json[i])[1] < low:
            low = (data_json[i])[1]

    high = (data_json[0])[2]
    for i in range(numberofminutes-1):
        if (data_json[i])[2] > high:
            high = (data_json[i])[2]

    open = (data_json[numberofminutes-1])[3]
    close = (data_json[0])[4]

    volume = '????'

    print(low)
    print(high)
    print(open)
    print(close)

def createSqliteTable(nameofdbfile = 'candles_data.db', exchangeName = 'test', pair = 'BTCUSB', duration = '5m'):
    conn = sqlite3.connect(nameofdbfile)
    c = conn.cursor()

    setTableName = str(exchangeName + "_" + pair + "_" + duration)
    tableCreationStatement = """CREATE  TABLE  """ + setTableName + """(Id INTEGER  PRIMARY  KEY, date INT, high  REAL, low REAL, open  REAL, close REAL, volume  REAL, quotevolumeREAL, weightedaverageREAL,  sma_7 REAL,  ema_7  REAL,  sma_30  REAL, ema_30  REAL,  sma_200  REAL,  ema_200  REAL)"""

    c.execute(tableCreationStatement)



#refreshDataCandlee('BTCUSD', '5m')

"""
conn = sqlite3.connect('test.db')
c = conn.cursor()

#c.execute('''CREATE TABLE stocks (object text, price real)''')

c.execute('''INSERT INTO stocks VALUES('ballon' ,'10.99')''')
c.execute('''INSERT INTO stocks VALUES('ballon' ,'11.99')''')


t = ('ballon',)
c.execute('SELECT COUNT(*) FROM stocks WHERE object =?', t)
print(c.fetchone())
"""