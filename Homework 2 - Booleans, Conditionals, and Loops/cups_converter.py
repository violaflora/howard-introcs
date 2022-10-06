# Get the measurement and unit from the user. Do not modify these lines!
num_cups = float(input('Enter an amount in cups: '))
target_unit = input('Enter a unit to convert to (oz/pint/tbsp/ml): ')
if target_unit == "oz":
  new = num_cups * 8
  print(str(new) + " oz")
elif target_unit == "pint":
  new = num_cups / 2
  print(str(new) + " pint")
elif target_unit == "tbsp":
  new = num_cups * 16
  print(str(new) + " tbsp")
elif target_unit == "ml":
  new = num_cups * 207
  print(str(new) + " ml")
else:
  pass