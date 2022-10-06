import math
import string
import sys

def read_file(filename):
    """
    Given a filename, the fuction should read the text off the file;
    then, return a list of the lines of text in the file.
    """
    with open(filename) as fobj:
        a = fobj.readlines()
    return a

def get_words_from_string(line):
    """
    Given a line (string), the function should return a list of words in the line by
    i) converting each word to lower case
    ii) replacing each punctuation with a space

    Hint: You can use string.punctuation to check if a character is punctuation or not
    string.punctuation is merely a string of punctuations strung together

    Input: line (a string)
    Output: a list of strings/words where each string/word is a sequence of alphanumeric characters
    """
    line = line.lower()
    for char in line:
      if char in string.punctuation:
        line = line.replace(char, " ")
    return line.split()

def get_words_from_line_list(list_of_lines):
    """
    Given a list of line, parse the list of text lines into words.
    Return a list of all words found in the list of lines.

    Input: ["This the First-Line.", "This is the Second@Line."]
    Output: ["this", "the", "first", "line", "this", "is", "the", "second", "line"]

    Note that the output contains no punctuation/special characters such as "-" and "@",
    and each word is in lower case.
    Hint: You can make use of get_words_from_string(...) function define previously.
    """
    word_list = []
    for line in list_of_lines:
      word_list += get_words_from_string(line)
    return word_list

def count_frequency(word_list):
    """
    Given a list of words, return a dictionary
    where each word is a key and each word's count is its corresponding value

    Input: ["this", "is", "the", "first", "is", "line", "second", "line", "this"]
    Output: {
            "this": 2,
            "is": 2,
            "the": 1,
            "first": 1,
            "line": 2,
            "second": 1
        }
    """
    wordCount = {}
    for word in word_list:
      if word in wordCount:
        wordCount[word] += 1
      else:
        wordCount[word] = 1
    return wordCount

def find_most_common_word(freq_map):
    """
    Return the most common word in the dictionary
    Input: freq_map (dictionary)
    Output: the word with the highest frequency (str type)
    """
    highestcountFreq = 0
    mostCommonWord = ""
    for word in freq_map:
      if freq_map[word] > highestcountFreq:
        highestcountFreq = freq_map[word]
        mostCommonWord = word
    return mostCommonWord

def write_result(filename):
    """
    Given a filename, use previously defined functions to find the following values
    1)  number of lines in the file
    2)  number of words in the file
    3)  number of distinc words in the file
    4)  the most occuring word in the file

    write all these values to a text file called "result.txt"
    in the same order in 4 different lines.

    Eg: Input: filename-> "test.txt"
    Output written in the "result.txt":

    File: test.txt
    Number of lines: 1000
    Number of words: 8000
    Number of distinct words: 2000
    Most commonly used word: to
    """
    lines = read_file(filename)
    words = get_words_from_line_list(lines)
    distinctWords = count_frequency(words)
    mostOccuringWord = find_most_common_word(distinctWords)
    file = open("result.txt", "w")
    file.write("File: " + filename + "\n")
    file.write("Number of lines: " + str(len(lines)) + "\n") 
    file.write("Number of words: " + str(len(words))+ "\n")
    file.write("Number of distinct words: " + str(len(distinctWords)) + "\n")
    file.write("Most commonly used word: " + str(mostOccuringWord) + "\n")
    file.close()