def main():
    book = "books/frankenstein.txt"
    path = "./" + book

    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book} ---\n")
        countWords(file_contents)
        countCharacters(file_contents)
        print("--- End of report ---")
        

def countWords(words):
    wordCount = 0
    txt = words.split()
    for word in txt:
        wordCount += 1
    print(f"{wordCount} words found in the book!\n")

def countCharacters(book):
    dict = {}
    for char in book:
        if char.isalpha():

            if char in dict:
                dict[char] += 1
            else:
                dict[char.lower()] = 1
    for char in dict:
        print(f"the character '{char}' has been found {dict[char]} times!")

main()
