def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(countWords(file_contents))
        print(countCharacters(file_contents))


def countWords(words):
    wordCount = 0
    txt = words.split()
    for word in txt:
        wordCount += 1
    return wordCount

def countCharacters(book):
    dict = {}
    for char in book:
        if char.isalpha():

            if char in dict:
                dict[char] += 1
            else:
                dict[char.lower()] = 1
    print(dict)
    return type(dict)

main()
