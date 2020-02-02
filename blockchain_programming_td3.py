import requests
import json
import sqlite3
import os


def pause():
    programPause = input("Press the <ENTER> key to continue...")

# ====================================== FONCTION ======================================

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

def refreshDataCandles(pair = 'BTCUSB', duration = '5m'):

    numberofminutes = int(duration[0:(len(duration) - 1)])
    granularity = numberofminutes * 60

    adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/candles?granularity=' + str(granularity)
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
        c.execute("SELECT start_date FROM last_checks WHERE (table_name = '" + table_name + "' AND last_id = 0)")
        start_date = c.fetchone()[0]
        last_check = data_json[0][0]
        last_id = id - 1

        c.execute("INSERT INTO last_checks VALUES ('" + str(id) + "','" + exchange + "','" + trading_pair + "','" + duration + "','" + table_name + "','" + last_check + "','" + start_date + "','" + str(last_id) + "')")

        conn.commit()
        conn.close

        # endregion

    else:
        print("Pas de nouvelles données à rajouter")

def getLast300Candles(pair = 'BTCUSB', duration = '5m'):

    numberofminutes = int(duration[0:(len(duration) - 1)])
    granularity = numberofminutes * 60
    print(granularity)

    adress = 'https://api.pro.coinbase.com/products/' + pair[0:3] + '-' + pair[3:6] + '/candles?granularity=' + str(granularity)

    data = requests.get(adress)
    data_json = json.loads(data.text)

    for i in range(300):

        date = data_json[299-i][0]
        low = (data_json[299-i])[1]
        high = (data_json[299-i])[2]
        open = (data_json[299-i])[3]
        close = (data_json[299-i])[4]
        volume = (data_json[299-i])[5]
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

    # region writing in our SQLite file named : "last_checks" (id, exchange, trading_pair, duration, table_name, last_check, startdate, last_id)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM last_checks")
    id = (c.fetchone())[0] + 1
    exchange = 'coinbase'
    trading_pair = pair
    duration = duration
    last_check = data_json[0][0]
    start_date = data_json[299][0]
    last_id = 0

    c.execute("INSERT INTO last_checks VALUES ('" + str(
        id) + "','" + exchange + "','" + trading_pair + "','" + duration + "','" + table_name + "','" + str(last_check) + "','" + str(start_date) + "','" + str(last_id) + "')")

    conn.commit()
    conn.close

    # endregion

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
        print("table does not exist")
        return False
    else:
        #print("table already exist")
        return True

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
        print('4 - Créer ou actualiser un SQLite avec les candles d une pair spécifique')
        print('5 - Récuperer "all available trade data" et le stocker dans un SQLite')
        print('0 - Exit')
        print("\n" + "Saisir l'action que vous souhaitez réaliser.")

        choix = input()
        if(choix == '1'):
            os.system("cls")
            getAvailableCryptocurrencies()

        elif(choix == '2'):
            os.system("cls")
            print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
            select_pair = input()
            print("Veuillez saisir ce que vous souhaitez (ex : bid)")
            select_direction = input()
            if(select_direction == str('ask') or select_direction == str('bid')):
                getDepth(select_direction, select_pair)
            else:
                print("Données rentrées incorrecte")

        elif(choix == '3'):
            os.system("cls")
            print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
            select_pair = input()
            print("Veuillez saisir ce que vous souhaitez (ex : bid)")
            select_direction = input()
            if (select_direction == str('ask') or select_direction == str('bid')):
                getOrderBook(select_direction, select_pair)
            else:
                print("Données rentrées incorrecte")

        elif(choix == '4'):
            os.system("cls")
            print("Veuillez saisir la pair que vous souhaitez (ex : BTCUSD)")
            select_pair = input()
            print("Veuillez saisir la 'duration' souhaitez (choix : 5m / 15m / 60m / 360m / 1440m)")
            select_duration = input()
            if (select_duration != str('1m') or select_duration != str('5m') or select_duration != str('5m') or select_duration != str('15m') or select_duration != str('60m') or select_duration != str('360m') or select_duration != str('1440m')):
                #verifier qu'une table n'existe pas déjà
                table_name = str("coinbase_" + select_pair + "_" + select_duration)
                if(DoesTheTableAlreadyExist(table_name) == False):
                    getLast300Candles(select_pair, select_duration)
                else:
                    refreshDataCandles(select_pair, select_duration)

            else:
                print("Données rentrées incorrecte")

        elif(choix == '5'):
            os.system("cls")

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