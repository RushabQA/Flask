string = input("Enter a comma separeted string: ")

words = string.split(",")

words.sort()

print(",".join(words))