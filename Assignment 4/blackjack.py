#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11.
    in the function bust: add these three numbers together.
    if they add up to or less than 21, return the sum.
    If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''

def bust(num1, num2, num3):
    #in the function bust: add these three numbers together.
    #if they add up to or less than 21, return the sum.
    if num1 + num2 + num3 <= 21:
        return(num1 + num2 + num3)
    #If it's over 21 BUT there's an 11 as one of the values, return the sum - 10.
    elif num1 + num2 + num3 == 11:
        return(num1 + num2 + num3 - 10)
    #if they add up to or less than 21, return the sum.
    else:
        return(0)

def main():
    # generate random integer values
    from random import seed
    from random import randint

    # seed random number generator
    seed()
    # generate some integers
    for _ in range(11):
        num1 = randint(0, 11)
        num2 = randint(0, 11)
        num3 = randint(0, 11)

    print(bust(num1, num2, num3))
main()
