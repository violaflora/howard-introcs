def reverse_vowels(phrase):
    vowels = ""
    newString = ""
    vowelString = "aeiou"
    for char in phrase:
      if char in vowelString:
        vowels = vowels + char
    for char in phrase:
      if char in vowelString:
        newString = newString + vowels[-1]
        vowels = vowels[:-1]
      else:
        newString = newString + char
    return newString
    

if __name__ == "__main__":
  print(reverse_vowels('computer science'))
  