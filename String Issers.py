# For advanced data validation, we can use string issers!

# Here's a sample so you can try this
sUserInput = input("Enter whatever you'd like: ")

# alnum stands for alphanumeric, which means either letters or numbers (or both) are present
print(f"\nIs \"{sUserInput}\" alphanumeric?: {sUserInput.isalnum()}")

# You can also use .isdecimal() and isdigit() for this exercise
print(f"Does \"{sUserInput}\" contain only numbers?: {sUserInput.isnumeric()}")

# alpha meaning alphabet (A-Z)
print(f"Does \"{sUserInput}\" contain only letters A-Z?: {sUserInput.isalpha()}")

# Is either all lowercase or all uppercase
print(f"Does \"{sUserInput}\" contain only lowercase letters?: {sUserInput.islower()}")
print(f"Does \"{sUserInput}\" contain only uppercase letters?: {sUserInput.isupper()}")

# Ccould the string be a valid Python variable name
print(f"Could \"{sUserInput}\" be a variable name?: {sUserInput.isidentifier()}")

# Finally, could the string be empty
print(f"Is \"{sUserInput}\" an empty string?: {sUserInput == ""}")
