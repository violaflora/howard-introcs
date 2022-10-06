import book_analysis

book_analysis.write_result("code/verne.txt")

with open("result.txt", "r") as f:
  lines = f.readlines()
  if len(lines) < 5:
    print("Your output file does not contain enough lines. Should have at least 5.")

  if lines[0].strip() != "File: code/verne.txt":
    print("First line should be 'File: verne.txt', but yours is " + lines[0])
    
  if lines[1].strip() != "Number of lines: 1057":
    print("Second line should be 'Number of lines: 1057', but yours is " + lines[1])
    
  if lines[2].strip() != "Number of words: 8943":
    print("Third line should be 'Number of words: 8943', but yours is " + lines[2])
    
  if lines[3].strip() != "Number of distinct words: 2150":
    print("Fourth line should be 'Number of distinct words: 2150', but yours is " + lines[3])
    
  if lines[4].strip() != "Most commonly used word: the":
    print("Fifth line should be 'Most commonly used word: the', but yours is " + lines[4])
    
  print("Passed!")