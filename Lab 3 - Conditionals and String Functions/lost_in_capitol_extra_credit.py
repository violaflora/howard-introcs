# Capitol Maps: Find your way around D.C.!

# Please use this module to write your code for Extra Credit Test
import math
lat = input("Insert your latitude: ")
longitude = input("Insert your longitude: ")

latlegsq = ((38.921669 - float(lat)) * 69)**2
longitudelegsq = ((-77.021361 - float(longitude)) * 53)**2
distance = math.sqrt(latlegsq + longitudelegsq)
distanceround = round(distance, ndigits = 1)

print("\nYou are " + str(distanceround) + " miles from Downing Hall")