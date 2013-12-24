from currency import Currency

print("\t-----------------------------------------------------")
print("\tWELCOME TO TEST BED FOR PROJ 10 - CURRENCY CONVERSION")
print("\t-----------------------------------------------------")

print("------------------------------------------------------------------------------------")
print("TC1: Create a new valid currency type and print it")
curr1 = Currency(100, 'USD')
print(curr1)

print("------------------------------------------------------------------------------------")
print("TC2: Create a new invalid currency type and print it")
curr1 = Currency(200, 'xyz')
print(curr1)

print("------------------------------------------------------------------------------------")
print("TC3: Convert a currency to another and print both")
curr1 = Currency(200, 'USD')
curr2 = curr1.convert_to('SEK')
print(curr1)
print(curr2)

print("------------------------------------------------------------------------------------")
print("TC4: Adding two currency amounts")
curr1 = Currency(100, 'USD')
curr2 = Currency(1316, 'SEK')
print(curr1+curr2)

print("------------------------------------------------------------------------------------")
print("TC5: Adding a currency amount and an int")
curr1 = Currency(100, 'USD')
print(curr1+10)

print("------------------------------------------------------------------------------------")
print("TC6: Adding a currency amount and a float")
curr1 = Currency(100, 'USD')
print(curr1+20.53)

print("------------------------------------------------------------------------------------")
print("TC7: Adding an int and a currency amount")
curr1 = Currency(100, 'USD')
print(50+curr1)

print("------------------------------------------------------------------------------------")
print("TC8: Adding a float and a currency amount")
curr1 = Currency(100, 'USD')
print(25.5+curr1)

print("------------------------------------------------------------------------------------")
print("TC9: Subtracting two currency amounts")
curr1 = Currency(300, 'USD')
curr2 = Currency(1316, 'SEK')
print(curr1-curr2)

print("------------------------------------------------------------------------------------")
print("TC10: Subtracting a currency amount and an int")
curr1 = Currency(100, 'USD')
print(curr1-10)

print("------------------------------------------------------------------------------------")
print("TC11: Subtracting a currency amount and a float")
curr1 = Currency(100, 'USD')
print(curr1-20.53)

print("------------------------------------------------------------------------------------")
print("TC12: Subracting an int and a currency amount")
curr1 = Currency(100, 'USD')
print(50-curr1)

print("------------------------------------------------------------------------------------")
print("TC13: Subtracting a float and a currency amount")
curr1 = Currency(100, 'USD')
print(25.5-curr1)

print("------------------------------------------------------------------------------------")
print("TC14: Checking __gt__ for true condition")
curr1 = Currency(300, 'USD')
curr2 = Currency(1316, 'SEK')
print(curr1>curr2)

print("------------------------------------------------------------------------------------")
print("TC15: Checking __gt__ for false condition")
curr1 = Currency(100, 'USD')
curr2 = Currency(1300, 'SEK')
print(curr1>curr2)

print("------------------------------------------------------------------------------------")
print("TC16: Checking __repr__")
curr1 = Currency(100, 'USD')
print(repr(curr1))