

def printHello():
    print("Hello")
    
def printName(x):
    print(x)
    
def addition(x, y):
    #add x and y together and return them
    return(x + y)

def smaller(i, j):
    #if i is smaller than j, return i
    if i < j:
        return(j)
    #if j is smaller than i, return j
    elif j < i:
        return(i)
    #if they're even, return 0
    else:
        return(0)

def main():
    
    #call the printHello function here
        printHello()

    #call printName and give it the parameter of your name
        name = "riley"
        printName(name)

        var1= 10
        var2= 20
    #What do we put in here to make it work?
        print(addition(var1, var2))
    
        num1 = int(input("Enter number 1"))
        num2 = int(input("Enter number 2"))
    #what go here?
        print(smaller(num1, num2))


main()

