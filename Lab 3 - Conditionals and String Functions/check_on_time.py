#Please write your code here for Check on Time lab problem.
arrival_time = input("Enter your arrival time in HH:MM format: ") # Asking a user to provide their arrival time in HH:MM format

hours, minutes = arrival_time.split(":") # extracting hours and minutes. 
# split(":") returns a list of strings splitting strings seperated by ":". 
# We will learn about lists, and unpacking variables later in this class.
print("You arrived at " + str(hours) + ":" + str(minutes) + ".")
hours = int(hours) # converting string type hours to int type
minutes = int(minutes) # converting string type minutes to int type

# Print out what time the student arrived. 

# Let the student know if they are late ocr on time.
if int(hours) < 9:
  print("You are on time!")
elif int(hours) == 9:
  if int(minutes) == 0:
    print("You are on time!")
  elif int(minutes) >= 11:
    print("VERY late. Yikes.")
  else:
    print("You are late.")
if hours > 9:
  print("VERY late. Yikes.")