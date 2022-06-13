Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #name = input(Enter the name of the expense:")
>>> #input name monthlycharge = flot(input("Enter monthly charge:"))
>>> #convert to float and input monthly = 0.060*monthlycharge
>>> #calculate monthly tax amountmonthly = monthlycharge + monthly
>>> #add tax to monthlycharge amountyearly = amountmonthly*12.00
>>> #calculate yearly charge
>>> print("Bill:"+'name'+"------Before tax:$"+'monthlycharge')
Bill:name------Before tax:$monthlycharge
>>> print("monthly tax:\t\t$"+'round''monthlytax,2')
monthly tax:		$roundmonthlytax,2
>>> #display the monthly tax after rounding
>>> print("monthly Charge:\t\t$"+'round''amountmonthly,2)
      
SyntaxError: EOL while scanning string literal
>>> print("monthly Charge:\t\t$"+'round''amountmonthly,2')
monthly Charge:		$roundamountmonthly,2
>>> #display the monthly charge after rounding
>>> print("Annual Charge:\t\t$"+'round''amountyearly,3')
Annual Charge:		$roundamountyearly,3
>>> #display the annual charge after rounding