# Get a passcode from the user. Do not modify this line!
passcode = int(input('Passcode? '))

if len(str(passcode)) == 8 or len(str(passcode)) == 9:
  print("Passcode is secure.")
elif len(str(passcode)) >= 4 and len(str(passcode)) <= 7:
  print("Passcode is not secure.")
else:
  print("Invalid passcode.")