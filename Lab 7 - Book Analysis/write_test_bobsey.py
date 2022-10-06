import book_analysis

book_analysis.write_result("code/bobsey.txt")

with open("result.txt", "r") as f:
  lines = f.readlines()
  if len(lines) < 5:
    print("Your output file does not contain enough lines. Should have at least 5.")

  if lines[0].strip() != "File: code/bobsey.txt":
    print("First line should be 'File: bobsey.txt', but yours is " + lines[0])
    
  if lines[1].strip() != "Number of lines: 6667":
    print("Second line should be 'Number of lines: 6667', but yours is " + lines[1])
    
  if lines[2].strip() != "Number of words: 49785":
    print("Third line should be 'Number of words: 49785', but yours is " + lines[2])
    
  if lines[3].strip() != "Number of distinct words: 3354":
    print("Fourth line should be 'Number of distinct words: 3354', but yours is " + lines[3])
    
  if lines[4].strip() != "Most commonly used word: the":
    print("Fifth line should be 'Most commonly used word: the', but yours is " + lines[4])
    
  print("Passed!")
