#Instructions: Create a variable of any name and set it equal to 10.
#The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
#The else should read: Else print out "10 is less than 10"

def main():

#Instructions: Create a variable of any name and set it equal to 10.
    spoon = 10

#The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
    if spoon > 12:
        print(spoon, "is greater than 12")

#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
    elif spoon > 11:
        print(spoon,  "is greater than 11")

#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
    elif spoon == 10:
        print(spoon, "is equal to 10")

#The else should read: Else print out "10 is less than 10"
    else:
        print(spoon, "is less than 10")
main()
