
#These instructions below are copied fromt the other example, the adjustments are a space after
#Instructions: Create a variable of any name and set it equal to 10.
#The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
#The else should read: Else print out "10 is less than 10"


def main():

    #Instructions: Create a variable of any name and set it equal to 10.
    #additional instructions: instead of setting our variable to 10, what if we asked the user for the variable and used that value in our comparisons?
    number = input("Insert a number")
    number = int(number)

    #The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
    if number > 12:
        print(number , "is greater than 12")
    # The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
    elif number > 11:
        print(number , "is greater than 11")
    #The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
    elif number == 10:
        print(number , "is 10")
    #The else should read: Else print out "10 is less than 10"
    else:
        print(number, "is less than 10")

main()
