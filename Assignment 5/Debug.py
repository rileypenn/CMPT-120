def main():
   # good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")

    # can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")


    # what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")

    # good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")

    # now write code to check if the input was either an asterisk OR an ampersand (&)
    asterAmperInput = input("Enter an asterisk or an ampersand")
    if asterAmperInput == "*":
        print("Asterisk")
    elif asterAmperInput == "&":
        print("Ampersand")
    else:
        print("smh follow directions")


    # do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    integerInput = input("enter an integer")
    if integerInput.isnumeric():
        print("yes")
    else:
        print("no")

    # last challenge: find out how to check if the string input has the substring "marist"
    # google this one ;) substring is the key google term
    maristString= "marist"
   
    if "need" in maristString:
        print("Yes! it is present in the string")
    else:
        print("No! it is not present")


main()
