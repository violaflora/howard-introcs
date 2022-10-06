#prompt the user to enter a whole number 
number = input("Enter a whole number: ")

#calculate the two values, x egg cartons full and y eggs left over
full = int(number)//12
left = int(number)%12

#print the two values; first x egg cartons full, then y eggs left over 
print(str(full) + " egg cartons full")
print(str(left) + " eggs left over")