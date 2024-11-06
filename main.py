def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(countWords(file_contents))


def countWords(words):
    wordCount = 0
    txt = words.split()
    for word in txt:
        wordCount += 1
    return wordCount

main()
