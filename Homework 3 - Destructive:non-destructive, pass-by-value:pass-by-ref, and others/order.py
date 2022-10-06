def same_order(original, sample):
  upper = ""
  if len(original) == 0:
    boo = False
  if len(sample) == 0:
    boo = True
  for char in original:
    if char.isupper():
      upper += char
  if sample == upper:
    boo = True
  else:
    boo = False
  return boo
    

if __name__ == "__main__":
  print(same_order('abCdODzIgNbevG', 'HELLO')) # False
  print(same_order('abCdODzIgNbevG', 'CODING'))# True
