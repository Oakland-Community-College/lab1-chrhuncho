def str_scramble(word):
    new_word = ""
    i = 0
    while i < len(word):
        if i % 2 == 0:
            if (i + 1) < len(word):
                new_word += word[i+1]
            elif i + 1 == len(word):
                new_word += word[i]
        else:
            new_word += word[i-1]
        i += 1
    print(new_word)


wordIn = input("Enter a word to scramble: ")
str_scramble(wordIn)