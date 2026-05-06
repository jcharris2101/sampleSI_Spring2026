# Almost everything you can do with a list, you can do with a string!

sSentence = "The quick brown fox jumps over the lazy dog"

# length of a string
print(len(sSentence))

# You can also access an index from a string, and even slice it!
print(sSentence[2])
print(sSentence[0:4])

# Finally, there's also nothing stopping you from looping through a string, character-by-character
for sChar in sSentence:
    print(sChar)