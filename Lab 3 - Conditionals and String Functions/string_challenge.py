# Please write your code here for "Tests for String Challenge"
input_string = input()

count = 0
output = ""
for i in range(len(input_string)):
  letter = input_string[i]
  prev_letter = input_string[i-1]
  if i == 0:
    output += input_string[i]
    count = 1
  elif letter == prev_letter:
    output += input_string[i]
    count += 1
  else:
    output += str(count)
    count = 1
    output += input_string[i]
  if i == len(input_string) - 1:
    output += str(count)

print(output)