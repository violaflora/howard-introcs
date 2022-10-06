# Write a program which asks the user for student grades until the user types "done".
# The program should then compute the mean and median grades for all the students, rounded to two decimal places.
# See the instructions for further details.
grades = []

def mean(grades):
    sumgrades = sum(grades)
    meangrades = round(sumgrades/len(grades), 2)
    return meangrades
    
def median(grades):
    grades.sort()
    if len(grades) % 2 == 1:
        med = grades[int((len(grades) + 1) / 2) - 1]
    else:
        even1 = grades[int(len(grades) / 2)]
        even2 = grades[int((len(grades) / 2) - 1)]
        med = (even1 + even2) / 2
    return med
    
# You also need to implement the rest of the code for run() below: 
def run():
    getting_input = True
    grades = []
    
    while getting_input:
        inp = input("Next grade: ")
        if inp == "done":
            getting_input = False
        else: 
            # Here you can prompt a user to enter the next grade and update your list of grades 
            grades.append(float(inp))
    print("Mean: " + str(mean(grades)))
    print("Median: " + str(median(grades)))
    

if __name__ == "__main__":
    run()