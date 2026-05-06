# Like with files, lists have functions attached to them
# We access these functions in the exact same way we access .readline(), and .write()

# This file will show you how to add to a list using .append()!

def main():
    # This list will start out empty - we're going to add data to it!
    sNames = []

    # This loop will allow you to add as many names to the list above as you like
    while True:
        sNameToAdd = input("Add a name to the list (enter 999 to quit): ").title()

        if sNameToAdd == "999":
            break

        # Here's how we add to the list!
        sNames.append(sNameToAdd)

    # If there's anything in the list, do the following:
    if len(sNames) > 0:
        # Sort the data in the list
        sNames.sort()

        print("Here's the names you entered (sorted):")

        for sCurrentName in sNames:
            print(sCurrentName)

    else:
        print("You didn't enter anything into the list!")

main()