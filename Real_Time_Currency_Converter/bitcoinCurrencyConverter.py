#Project 1.1 - Bitcoin Currency Converter

#Imports
from forex_python.bitcoin import BtcConverter
from datetime import datetime

#date_obj = datetime.datetime(2021,3,9,16,40,0,815417)
current_day = int(datetime.now().strftime('%d'))

if current_day > 1 :
    day = current_day - 1

date_obj = datetime.now().strftime("%Y-%m-" + str(day) +" %H:%M:%S.%f")
#2018-05-18 19:39:36.815417
date = datetime.strptime(date_obj, '%Y-%m-%d %H:%M:%S.%f')
c = BtcConverter()

#Input
amount = int(input("Enter the amount for converter: "))
currency = input("Enter the currency: ").upper()
result = c.convert_to_btc(amount,currency)

#Output
print(result)
print("\nThe price of 1 bitcoin in " + str(date) + " in " + currency + " was " + str(c.get_previous_price(currency, date)))
