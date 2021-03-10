#Project 1 - Real Time Currency Rates

#Imports
from forex_python.converter import CurrencyRates

c = CurrencyRates()

#Input
amount = int(input("Enter the amount for converter: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
result = c.convert(from_currency,to_currency,amount)

#Output
print(result)
