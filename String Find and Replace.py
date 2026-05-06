# You can look up the location of certain characters, and you can also replace characters!

# This sentence contains every letter in the alphabet
sSentence = "The quick brown fox jumps over the lazy dog"

# Using the .find() method, you can locate the first index where a letter is found
print(f"The letter \"e\" is first found at index {sSentence.find("e")}")

# .find() will return a -1 if it cannot find the specified argument in the string
# NOTE: You can also use .index() for this, but that function raises a ValueError if it cannot find an index

# To find every instance of a letter, you don't use .find(). Instead you can use a loop and some if-logic:
sCharToFind = "o"

for iPosition in range(0, len(sSentence)):
    sChar = sSentence[iPosition]

    if sChar == sCharToFind:
        print(f"The letter \"{sCharToFind}\" was found at index: {iPosition}.")

# You can replace every instance of one character in a string by using .replace()
sCharToReplace = "o"
sReplacement = "" # <-- leaving this blank will simply remove the character specified in sCharToReplace

print(f"Original sentence: {sSentence}")
print(f"Sentence after replacing \"{sCharToReplace}\" with \"{sReplacement}\": {sSentence.replace(sCharToReplace, sReplacement)}")

# Finally, there's nothing stopping you from chaining multiple functions together like this, which strips all vowels from the sentence:
print(f"Sentence with no vowels: {sSentence.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")}")

# pssssstttt, you can also do this (uncomment line below to see)
# print(f"Sentence with no vowels using list comprehension: {"".join([s for s in sSentence if s not in ["a", "e", "i", "o", "u"]])}")
