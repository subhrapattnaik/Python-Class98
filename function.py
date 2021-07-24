#write a program which takes file path from the user and prints the number of words in the file


def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()
