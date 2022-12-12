# Use number randomizer (1-4) to pick which variable will cause user to fall
from random import seed
from random import randint

seed()
for _ in range(4):
    wrongLimb = randint(1, 4)


    leftArm = 1
    leftLeg = 2
    rightArm = 3
    rightLeg = 4


class Climber:
    def __init__(self, name, age, attempt):
        self.name = name
        self.age = age
        self.attempt = attempt


def main():


# User inputs their name, age, and attempt at climbing
    userName = input("what is your name?")
    userAge = input("what is your age?")
    userAttempt = input("what attempt are you on?")


# User information is printed out
    climbingUser = Climber(userName, userAge, userAttempt)
    print(climbingUser.name, climbingUser.age, climbingUser.attempt)


# User instructions
    print("Welcome to the rock climbing wall! You will have four options at every point: choose between moving your left arm, left leg, right arm or right leg. Be careful when choosing- there's a chance you might slip and fall! Enjoy the climb!")
    print("Moving works as follows: Your left arm equals 1, your left leg equals 2, your right arm equals 3, and your right leg equals 4. Input one of these numbers in order to move up the wall.")


    move = 1
    # repeat this 10 times
    while (move < 10):
        wrongLimb = randint(1, 4)
        # User chooses which to move- rl, ra, ll, la
        movement = int(input("What do you move? 1, 2, 3, or 4?"))
        # check user input
        if movement > 5:
            print("Please enter valid instructions in order to climb")
            break
        # if user moves wrongLimb first, have them fall
        if movement == wrongLimb:
            print("Oh no! You fell off :( Restart?")
            break
        # if user moves any of the others first, proceed
        elif movement != wrongLimb:
            print("You've successfully moved up!")
        else:
            print("huh o.0")
        move += 1


    # if user makes it through 10 inputs without falling, they reach the top of the wall and win
    # when user wins, display end message
    if move == 10:
        print("Congrats, you climbed the wall!")


main()





