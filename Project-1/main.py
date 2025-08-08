# take input of word
word = input("Enter a word: ")
# take input of character
char = input("Enter a character: ")
i = 0
count = 0
# loop will find the occurrence of a character in the word
while i < len(word):
    if word[i] == char:
        count += 1  # increment count
    i += 1  # increment index
# display the result with style formatting
print(f"\033[1;34m{char} occurs {count} times in {word}\033[0m")