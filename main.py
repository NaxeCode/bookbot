def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(countWords(file_contents))


def countWords(words):
    wordCount = 0
    for word in words:
        wordCount += 1
    return wordCount

main()
