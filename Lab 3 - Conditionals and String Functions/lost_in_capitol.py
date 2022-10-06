# Capitol Maps: Find your way around D.C.!

# Please use this module for "Tests for Lost in Capitol" autograder tests.
lat = input("Insert your latitude: ")
longitude = input("Insert your longitude: ")

# Check for north or south of K St
if float(lat) > 38.902649:
  print("You are north of K St")
else:
  print("You are south of K St")

# Check for north or south of White House
if float(lat) > 38.897789:
  print("You are north of the White House")
elif float(lat) < 38.897789:
  print("You are south of the White House")
else:
  pass

# Check for east or west of White House
if float(longitude) > -77.036562:
  print("You are east of the White House")
elif float(longitude) < -77.036562:
  print("You are west of the White House")
else:
  pass

# Check for north or south of Downing Hall
if float(lat) > 38.921669:
  print("You are north of Downing Hall")
elif float(lat) < 38.921669:
  print("You are south of Downing Hall")
else:
  pass

# Check for east or west of Downing Hall
if float(longitude) > -77.021361:
  print("You are east of Downing Hall")
elif float(longitude) < -77.021361:
  print("You are west of Downing Hall")
else:
  pass

# Check for north or south of Dupont Circle
if float(lat) > 38.909760:
  print("You are north of Dupont Circle")
elif float(lat) < 38.909760:
  print("You are south of Dupont Circle")
else:
  pass

# Check for east or west of Dupont Circle
if float(longitude) > -77.043479:
  print("You are east of Dupont Circle")
elif float(longitude) < -77.043479:
  print("You are west of Dupont Circle")
else:
  pass

# Check for north or south of Union Station
if float(lat) > 38.897698:
  print("You are north of Union Station")
elif float(lat) < 38.897698:
  print("You are south of Union Station")
else:
  pass

# Check for east or west of Union Station
if float(longitude) > -77.007200:
  print("You are east of Union Station")
elif float(longitude) < -77.007200:
  print("You are west of Union Station")
else:
  pass