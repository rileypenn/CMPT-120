'''
mkay so
I talked a lot about helping but not fixing the problem
In this code, if you run this and enter not an integer, it throws an error, as we're aware, as you solved this problem in the debug file
can you google a way to help or even fix this problem that isn't the way we were doing it before?
hint: there's try/catch statements that i didn't teach but is somewhat straightforward to try. There's a thing called regex, etc.
You can also go much much simpler if you want to, I just want you guys to keep practicing your google skills
and ofc, if you're stuck, don't hesitate to email
'''


def main():
    intInput = input("Enter an int")

    if intInput == intInput.isnumeric():
        print("Wow a number!")
    elif intInput == intInput.isalpha():
        print("Input an integer!")
    else:
        print("What did you do")

main()
