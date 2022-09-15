def main():

    name = "Riley"

    if name == "riley":
        print(name)
    elif name == "Riley":
        print(name)
    else:
        print("Who are you?")

    seven = 7
    eight = 8

    if seven == eight:
        print("Equal")
    else:
        print("Not Equal")

    four = 4

    if four > 5:
        print("Too big")
    elif four > 0 and four < 5:
        print("Just right")
    else:
        print("Too small")

    age = input("How old are you?")
    age = int(age)

    if age <= 21:
        print("You're too young.")
    else:
        print("Enjoy!")

    # % = modulo/modulus, essentially repeated subtraction until there is a remainder
    number = 1000
    if number % 2 == 0:
        print(number, " is even")
    else:
        print(number, "is odd")

main()
