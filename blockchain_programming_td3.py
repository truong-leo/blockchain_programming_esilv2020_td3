import requests
import json
import sqlite3
import os
import datetime

def pause():
    programPause = input("Press the <ENTER> key to continue...")

# ====================================== FONCTION ======================================

def getAvailableCryptocurrencies():
    products = requests.get('https://api.pro.coinbase.com/products')
    products_json = json.loads(products.text)
    available_cryptocurrencies = 40 * [0]

    i = 0
    deja_present = False

    print("Voici la liste des cryptomonnaies échangeables :")

    for e in products_json:

        j = 0
        while j < 40:

            if (e['base_currency'] == available_cryptocurrencies[j]):
                deja_present = True
                break
            j += 1

        if (deja_present == False):
            available_cryptocurrencies[i] = e['base_currency']
            print(e['base_currency'])
            i = i + 1

        deja_present = False
    #print(available_cryptocurrencies)

def getAdressBook(pair = 'BTCUSD'):

    if (len(str(pair)) == 6):
        adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/book'
    if (pair == 'ATOMUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'USD' + '/book'
    if (pair == 'BATUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BAT' + '-' + 'USDC' + '/book'
    if (pair == 'DAIUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DAI' + '-' + 'USDC' + '/book'
    if (pair == 'MANAUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'MANA' + '-' + 'USDC' + '/book'
    if (pair == 'ETHUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ETH' + '-' + 'USDC' + '/book'
    if (pair == 'CVCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'CVC' + '-' + 'USDC' + '/book'
    if (pair == 'BTCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BTC' + '-' + 'USDC' + '/book'
    if (pair == 'LINKUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'USD' + '/book'
    if (pair == 'ALGOUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ALGO' + '-' + 'USD' + '/book'
    if (pair == 'GNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'GNT' + '-' + 'USDC' + '/book'
    if (pair == 'ZECUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ZEC' + '-' + 'USDC' + '/book'
    if (pair == 'LOOMUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LOOM' + '-' + 'USDC' + '/book'
    if (pair == 'LINKETH'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'ETH' + '/book'
    if (pair == 'DNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DNT' + '-' + 'USDC' + '/book'
    if (pair == 'ATOMBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'BTC' + '/book'
    if (pair == 'DASHUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'USD' + '/book'
    if (pair == 'DASHBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'BTC' + '/book'

    return adress

def getDepth(direction='ask', pair = 'BTCUSD'):
    adress = getAdressBook(pair)

    priceof = direction
    direction = direction + 's'
    data = requests.get(adress)
    data_json = json.loads(data.text)

    for e in data_json[direction]:
        print('The price of the ' + priceof + ' for ' + pair + ' is : ' + e[0])

    print('\n')

def getAdressOrderBook(pair = 'BTCUSD'):

    if (len(str(pair)) == 6):
        adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/book?level=2'
    if (pair == 'ATOMUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'USD' + '/book?level=2'
    if (pair == 'BATUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BAT' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'DAIUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DAI' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'MANAUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'MANA' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'ETHUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ETH' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'CVCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'CVC' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'BTCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BTC' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'LINKUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'USD' + '/book?level=2'
    if (pair == 'ALGOUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ALGO' + '-' + 'USD' + '/book?level=2'
    if (pair == 'GNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'GNT' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'ZECUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ZEC' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'LOOMUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LOOM' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'LINKETH'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'ETH' + '/book?level=2'
    if (pair == 'DNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DNT' + '-' + 'USDC' + '/book?level=2'
    if (pair == 'ATOMBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'BTC' + '/book?level=2'
    if (pair == 'DASHUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'USD' + '/book?level=2'
    if (pair == 'DASHBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'BTC' + '/book?level=2'

    return adress

def getOrderBook(direction='askorbid', pair = 'BTCUSD'):
    #adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/book?level=2'
    adress = getAdressOrderBook(pair)

    priceof = direction
    direction = direction + 's'
    data = requests.get(adress)
    data_json = json.loads(data.text)

    print("The first 50 values of the " + priceof + " order book are : " + "\n")

    print('%10s | %12s | %10s' % ('PRICE  ','SIZE    ','NUM-ORDERS'))
    print(35 * '_')
    for e in data_json[direction]:
        print('%10s | %12s | %5d' % (e[0],e[1],e[2]))

    print('\n')

def getAdress(pair = 'BTCUSD', duration = '5m', start = '2020-02-03T17:07:34', end = '2020-02-03T17:07:34'):
    numberofminutes = int(duration[0:(len(duration) - 1)])
    granularity = numberofminutes * 60

    if (len(str(pair)) == 6):
        adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'ATOMUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'USD' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'BATUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BAT' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'DAIUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DAI' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'MANAUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'MANA' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'ETHUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ETH' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'CVCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'CVC' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'BTCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BTC' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'LINKUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'USD' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'ALGOUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ALGO' + '-' + 'USD' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'GNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'GNT' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'ZECUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ZEC' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'LOOMUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LOOM' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'LINKETH'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'ETH' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'DNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DNT' + '-' + 'USDC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'ATOMBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'BTC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'DASHUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'USD' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)
    if (pair == 'DASHBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'BTC' + '/candles/?start=' + start + 'Z&end=' + end + 'Z&granularity=' + str(
            granularity)

    return adress

def getAdressTrades(pair = 'BTCUSD'):

    if (len(str(pair)) == 6):
        adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/trades'
    if (pair == 'ATOMUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'USD' + '/trades'
    if (pair == 'BATUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BAT' + '-' + 'USDC' + '/trades'
    if (pair == 'DAIUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DAI' + '-' + 'USDC' + '/trades'
    if (pair == 'MANAUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'MANA' + '-' + 'USDC' + '/trades'
    if (pair == 'ETHUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ETH' + '-' + 'USDC' + '/trades'
    if (pair == 'CVCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'CVC' + '-' + 'USDC' + '/trades'
    if (pair == 'BTCUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'BTC' + '-' + 'USDC' + '/trades'
    if (pair == 'LINKUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'USD' + '/trades'
    if (pair == 'ALGOUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ALGO' + '-' + 'USD' + '/trades'
    if (pair == 'GNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'GNT' + '-' + 'USDC' + '/trades'
    if (pair == 'ZECUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ZEC' + '-' + 'USDC' + '/trades'
    if (pair == 'LOOMUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LOOM' + '-' + 'USDC' + '/trades'
    if (pair == 'LINKETH'):
        adress = 'https://api.pro.coinbase.com/products/' + 'LINK' + '-' + 'ETH' + '/trades'
    if (pair == 'DNTUSDC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DNT' + '-' + 'USDC' + '/trades'
    if (pair == 'ATOMBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'ATOM' + '-' + 'BTC' + '/trades'
    if (pair == 'DASHUSD'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'USD' + '/trades'
    if (pair == 'DASHBTC'):
        adress = 'https://api.pro.coinbase.com/products/' + 'DASH' + '-' + 'BTC' + '/trades'

    return adress

def refreshDataCandles(pair = 'BTCUSD', duration = '5m'):

    #numberofminutes = int(duration[0:(len(duration) - 1)])
    #granularity = numberofminutes * 60

    actual_date = datetime.datetime.now().isoformat()
    start = datetime.datetime.now() - datetime.timedelta(days=1, hours=1, minutes=0, seconds=0)
    end = start + datetime.timedelta(days=1, hours=1, minutes=0, seconds=0)

    adress = getAdress(pair, duration, start.isoformat()[0:19], end.isoformat()[0:19])

    data = requests.get(adress)
    data_json = json.loads(data.text)

    table_name = str("coinbase_" + pair + "_" + duration)

    #SQL PART

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("SELECT date FROM " + table_name +" WHERE id = (SELECT MAX(id) FROM " + table_name + ")")
    last_date = c.fetchone()[0]

    conn.commit()
    conn.close

    print("Last date : " + str(last_date))
    print("Premiere nouvelle date : " + str(data_json[0][0]))

    if(str(last_date) != str(data_json[0][0])):

        j = 0
        how_many_new_data = 0
        while(last_date != data_json[j][0]):
            how_many_new_data += 1
            j += 1

        #how_many_new_data = how_many_new_data - 1
        print("Nb de nouvelles données à rajouter :" + str(how_many_new_data))

        i = 1
        while(how_many_new_data >= 1 and (how_many_new_data - i) >= 0):

            date = data_json[how_many_new_data - i][0]
            low = (data_json[how_many_new_data - i])[1]
            high = (data_json[how_many_new_data - i])[2]
            open = (data_json[how_many_new_data - i])[3]
            close = (data_json[how_many_new_data - i])[4]
            volume = (data_json[how_many_new_data - i])[5]
            opendate = date

            # SQL PART

            conn = sqlite3.connect('data.db')
            c = conn.cursor()

            # region writing our data in "exchangeName_pair+_duration" (id, date, high, low, open, close, volume)

            table_name = str("coinbase_" + pair + "_" + duration)

            if (DoesTheTableAlreadyExist((table_name)) == False):
                print("Creation of a new table")
                tableCreationStatement = """CREATE  TABLE  """ + table_name + """(Id INTEGER  PRIMARY  KEY, date INT, high  REAL, low REAL, open  REAL, close REAL, volume  REAL)"""
                c.execute(tableCreationStatement)

            c.execute("SELECT COUNT(*) FROM " + table_name)
            res = c.fetchone()
            id2 = res[0] + 1
            print("Creating ID : " + str(id2))

            c.execute("INSERT INTO " + table_name + " VALUES ('" + str(id2) + "','" + str(opendate) + "','" + str(high) + "','" + str(low) + "','" + str(open) + "','" + str(close) + "','" + str(volume) + "')")

            conn.commit()
            conn.close

            how_many_new_data -= 1

        # region writing in our SQLite file named : "last_checks" (id, exchange, trading_pair, duration, table_name, last_check, startdate, last_id)

        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM last_checks")
        id = (c.fetchone())[0] + 1
        exchange = 'coinbase'
        trading_pair = pair
        duration = duration
        c.execute("SELECT startdate FROM last_checks WHERE (table_name = '" + table_name + "' AND last_id = 0)")
        start_date = c.fetchone()[0]
        last_check = data_json[0][0]
        c.execute("SELECT MAX(Id) FROM last_checks WHERE (table_name = '" + table_name + "')")
        last_id = (c.fetchone())[0]

        c.execute("INSERT INTO last_checks VALUES ('" + str(id) + "','" + str(exchange) + "','" + str(trading_pair) + "','" + str(duration) + "','" + str(table_name) + "','" + str(last_check) + "','" + str(start_date) + "','" + str(last_id) + "')")

        conn.commit()
        conn.close

        # endregion

    else:
        print("Pas de nouvelles données à rajouter")

def getLast300Candles(pair = 'BTCUSD', duration = '5m', profondeur = 1):

    actual_date = datetime.datetime.now().isoformat()
    start = datetime.datetime.now() - profondeur * datetime.timedelta(days=1, hours = 1, minutes = 0, seconds = 0)
    end = start + datetime.timedelta(days=1, hours = 1, minutes = 0, seconds = 0)

    for j in range(profondeur):

        adress = getAdress(pair, duration, start.isoformat()[0:19], end.isoformat()[0:19])

        data = requests.get(adress)
        data_json = json.loads(data.text)
        nb_data = 0
        nb_data = len(data_json)

        for i in range(nb_data):

            date = data_json[nb_data-1-i][0]
            low = (data_json[nb_data-1-i])[1]
            high = (data_json[nb_data-1-i])[2]
            open = (data_json[nb_data-1-i])[3]
            close = (data_json[nb_data-1-i])[4]
            volume = (data_json[nb_data-1-i])[5]
            opendate = date

            #SQL PART

            conn = sqlite3.connect('data.db')
            c = conn.cursor()

            #region writing our data in "exchangeName_pair+_duration" (id, date, high, low, open, close, volume)

            table_name = str("coinbase_" + pair + "_" + duration)

            if(DoesTheTableAlreadyExist((table_name)) == False):
                print("Creation of a new table")
                tableCreationStatement = """CREATE  TABLE  """ + table_name + """(Id INTEGER  PRIMARY  KEY, date INT, high  REAL, low REAL, open  REAL, close REAL, volume  REAL)"""
                c.execute(tableCreationStatement)

            c.execute("SELECT COUNT(*) FROM " + table_name)
            res = c.fetchone()
            id2 = res[0] + 1
            print("Creating ID : " + str(id2))

            c.execute("INSERT INTO " + table_name + " VALUES ('" + str(id2) + "','" + str(opendate) + "','" + str(high) + "','" + str(low) + "','" + str(open) + "','" + str(close) + "','" + str(volume) + "')")

            conn.commit()
            conn.close

            #endregion

        start = end
        end = start + datetime.timedelta(days=1, hours = 1, minutes = 0, seconds = 0)

    # region writing in our SQLite file named : "last_checks" (id, exchange, trading_pair, duration, table_name, last_check, startdate, last_id)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    start = datetime.datetime.now() - profondeur * datetime.timedelta(days=1, hours=1, minutes=0, seconds=0)
    end = start + datetime.timedelta(days=1, hours=1, minutes=0, seconds=0)
    adress = getAdress(pair, duration, start.isoformat()[0:19], end.isoformat()[0:19])

    data = requests.get(adress)
    data_json = json.loads(data.text)
    nb_data = len(data_json)

    c.execute("SELECT COUNT(*) FROM last_checks")
    id = (c.fetchone())[0] + 1
    exchange = 'coinbase'
    trading_pair = pair
    duration = duration
    last_check = data_json[0][0]
    start_date = data_json[nb_data-1][0]
    last_id = 0

    c.execute("INSERT INTO last_checks VALUES ('" + str(
        id) + "','" + exchange + "','" + trading_pair + "','" + duration + "','" + table_name + "','" + str(
        last_check) + "','" + str(start_date) + "','" + str(last_id) + "')")

    conn.commit()
    conn.close

    # endregion


    print('\n')

def createSqliteTable(nameofdbfile = 'data.db', exchangeName = 'coinbase'):
    conn = sqlite3.connect(nameofdbfile)
    c = conn.cursor()

    # Keeping track of updates:
    c.execute("CREATE TABLE last_checks(Id INTEGER PRIMARY KEY, exchange TEXT, trading_pair TEXT, duration TEXT, table_name TEXT, last_check INT, startdate INT, last_id INT)")

    print("data.db file successfully created")
    # Data candles
    #setTableName = str(exchangeName + "_" + pair + "_" + duration)
    #tableCreationStatement = """CREATE  TABLE  """ + setTableName + """(Id INTEGER  PRIMARY  KEY, date INT, high  REAL, low REAL, open  REAL, close REAL, volume  REAL)"""
    #c.execute(tableCreationStatement)

def DoesTheTableAlreadyExist(nameofthetable):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + nameofthetable + "'")
    res = c.fetchone()

    if (res[0] == 0):
        print("Table does not exist")
        return False
    else:
        #print("table already exist")
        return True

def refreshData(pair = 'BTCUSD'):

    adress = getAdressTrades(pair)

    data = requests.get(adress)
    data_json = json.loads(data.text)
    nb_data = 0
    nb_data = len(data_json)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    table_name = str('coinbase_' + pair)
    if (DoesTheTableAlreadyExist((table_name)) == True):
        c.execute("DROP TABLE " + table_name)

    print("Creation of a new table")
    tableCreationStatement = """CREATE  TABLE  """ + table_name + """(Id INTEGER PRIMARY KEY, uuid TEXT, traded_btc REAL,  price REAL, created_at_int INT, side TEXT)"""
    c.execute(tableCreationStatement)

    conn.commit()
    conn.close

    for i in range(nb_data):

        uuid = str((data_json[nb_data - 1 - i])['trade_id'])
        traded_btc = (data_json[nb_data - 1 - i])['size']
        price = (data_json[nb_data - 1 - i])['price']
        created_at_int = (data_json[nb_data - 1 - i])['time']
        side = (data_json[nb_data - 1 - i])['side']

        # SQL PART

        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        # region writing our data in "exchangeName_pair" (id, uuid, traded_btc, price, created_at_int, side)

        c.execute("SELECT COUNT(*) FROM " + table_name)
        res = c.fetchone()
        id2 = res[0] + 1
        print("Creating ID : " + str(id2))

        c.execute("INSERT INTO " + table_name + " VALUES ('" + str(id2) + "','" + str(uuid) + "','" + str(
            traded_btc) + "','" + str(price) + "','" + str(created_at_int) + "','" + str(side) + "')")

        conn.commit()
        conn.close

        # endregion

    print('\n')

# ====================================== MENU ======================================
def menu():
    os.system("cls")
    choix = ''
    seed_present = False
    seed = ''

    while (choix != '0'):
        print("1 - Obtenir la liste des cryptomonnaies disponibles")
        print("2 - Obtenir le Ask ou le Bid d'un asset")
        print("3 - Obtenir l'order book d'un asset")
        print('4 - Créer ou actualiser un SQLite avec les candles d une paire spécifique')
        print('5 - Récuperer "all available trade data" et le stocker dans un SQLite')
        print('0 - Exit')
        print("\n" + "Saisir l'action que vous souhaitez réaliser.")

        choix = input()
        if(choix == '1'):
            os.system("cls")
            getAvailableCryptocurrencies()

        elif(choix == '2'):
            os.system("cls")
            try:
                print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
                select_pair = input()
                print("Veuillez saisir ce que vous souhaitez (ex : bid)")
                select_direction = input()
                if(select_direction == str('ask') or select_direction == str('bid')):
                    getDepth(select_direction, select_pair)
                else:
                    print("Données rentrées invalides")
            except (RuntimeError, TypeError, NameError, IOError, KeyError):
                print("Donneés rentrées invalides")

        elif(choix == '3'):
            os.system("cls")
            try:
                print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
                select_pair = input()
                print("Veuillez saisir ce que vous souhaitez (ex : bid)")
                select_direction = input()
                if (select_direction == str('ask') or select_direction == str('bid')):
                    getOrderBook(select_direction, select_pair)
                else:
                    print("Données rentrées invalides")
            except (RuntimeError, TypeError, NameError, IOError, KeyError):
                print("Donneés rentrées invalides")

        elif(choix == '4'):
            os.system("cls")
            try:
                print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
                select_pair = input()
                print("Veuillez saisir la 'duration' souhaitez (choix : 5m / 15m / 60m / 360m / 1440m)")
                select_duration = input()
                if (select_duration == str('1m') or select_duration == str('5m') or select_duration == str('5m') or select_duration == str('15m') or select_duration == str('60m') or select_duration == str('360m') or select_duration == str('1440m')):
                    #verifier qu'une table n'existe pas déjà
                    table_name = str("coinbase_" + select_pair + "_" + select_duration)
                    if(DoesTheTableAlreadyExist(table_name) == False):
                        print("Veuillez saisir la profondeur de l'historique des candles que vous souhaitez (ex : 10, alors il y aura un historique d'une taille maximum de 3000 candles). \n"
                              + "Si vous souhaitez un grand historique, le programme mettra un bon moment pour récupérer toutes les données. \n"
                              + "Pour tester et ne pas devoir attendre trop longtemps, un chiffre entre 1 et 10 est conseillé. +\n"
                              + "Note : il faut saisir un nombre entier > 0.")
                        profondeur = input()
                        if(profondeur == 0):
                            print("Veuillez saisir un nombre entier supérieur à 0.")
                        getLast300Candles(select_pair, select_duration)
                    else:
                        refreshDataCandles(select_pair, select_duration)

                else:
                    print("Données rentrées invalides")
            except (RuntimeError, TypeError, NameError, IOError, KeyError):
                print("Donneés rentrées invalides")

        elif(choix == '5'):
            os.system("cls")
            try:
                print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
                select_pair = input()
                refreshData(select_pair)

            except (RuntimeError, TypeError, NameError, IOError, KeyError):
                print("Donneés rentrées invalides")

        pause()
        os.system("cls")

    print("Au revoir !")

# ====================================== MAIN ======================================

def main():
    try:
        with open('data.db'):
            pass
    except IOError:
        createSqliteTable('data.db', 'coinbase')

    menu()

main()


