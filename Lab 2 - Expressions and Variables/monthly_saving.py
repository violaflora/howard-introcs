#prompt to enter monthly income
income = input("Enter your monthly income: ")

#prompt to enter total monthly rent
rent = input("Enter your monthly rent: ")

#prompt to enter total monthly grocery expense
grocery = input("Enter your grocery expenses: ")

#prompt to enter total internet bill
internet = input("Enter your internet bill: ")

#prompt to enter personal cell phone bill 
cell = input("Enter your cell phone bill: ")

#prompt to enter the cost for personal subscriptions such as Netflix, Amazon, 
subscriptions = input("Enter your miscellaneous expenses: ")

#calculate per head expenses out of the shared bills 


#calculate your total personal expenses 
total = float(rent) + float(grocery) + float(internet) + float(cell) + float(subscriptions)

#calculate monthly saving and print it 2 decimal places.
saving = float(income) - int(total)
saving = round(saving, 2)
print("Your monthly saving is " + str(saving))