#Prompt the user to enter a positive number 
num = input("Enter a positive integer: ")

#Implement the steps for Collatz conjecture using loop
modnum = int(num) % 2
if int(num) <= 0:
  exit()
if int(num) == 1:
  print(str(num))
  exit()
while num != 1:
  if modnum == 1:
    num = int(num) * 3 + 1
    print(str(num))
    num == int(num)
    modnum = int(num) % 2
  else:
    num = int(num) // int(2)
    print(str(num))
    num == int(num)
    modnum = int(num) % 2