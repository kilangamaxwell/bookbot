def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        splitted_lst = file_contents.split()
        word_count = len(splitted_lst)
        #print(word_count)

        file_contents = file_contents.lower()
        words_dict = {}
        for word in file_contents:
            if word not in words_dict.keys():
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        #print(words_dict)
        #print("\n")

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabets:
            if letter in words_dict.keys():
                print(f"The '{letter}' character was found {words_dict[letter]} times")

main()