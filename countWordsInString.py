def main():

    text = input("Please enter some text: ")
    myDict = {}

    for word in text.split():
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1

    longest_word_length = max(len(word) for word in myDict)
    for word in sorted(myDict):
        print("{:{}} : {}".format(word, longest_word_length, myDict[word]))
main()
