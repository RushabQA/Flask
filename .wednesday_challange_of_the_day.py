def str(word1, word2):
        if len(word1) != len(word2):
            return()
        else:
            new_word = ""
            for char1, char2 in zip(word1, word2):
                new_word += char1 + char2
            return(new_word)

