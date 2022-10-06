def remove_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    newWord = "".join(i for i in word if i not in vowels)
    return newWord

if __name__ == "__main__":
    print(remove_vowels("helloworld today is a good day"))