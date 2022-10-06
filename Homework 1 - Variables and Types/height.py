inches = input("What is your height in inches? ")
feet = int(inches) // 12
inches2 = int(inches) % 12
print("You are " + str(feet) + "ft" + str(inches2) + "in")