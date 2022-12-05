class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
# can you fill out the rest of this for me? im dumb
# the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return ("Domestic Longhair")
        else:
            return ("Domestic Shorthair")

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # create your own function! what do you want it to do?

class Egg:
    def __init__(self, style, cooked):
        self.style = style_of_egg
        self.cooked = how_long_cooked

def main():
    # fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog(Cooper, 5)
    print(dog1.name, dog1.age)

    # and what about a new employee
    employee1 = Employee(Fred, 204403, IT)
    # how would we print out each of the variables from newEmployee?
    print(employee1.name, employee1.idNumber, employee1.department)

    # now create and print out a cake you make
    cake1 = Cake(Carrot, vanilla)
    print(cake1.flavor, cake1.frosting)

    # and now create another cake and print it out
    cake2 = Cake(Chocolate, fudge)
    print(cake2.flavor, cake2.frosting)

    # create a cat!
    cat1 = Cat(Fuzzy, 12, long)
    print(cat1.name, cat1.age, cat1.fur_length)
    # create another cat!
    cat2 = Cat(Pikachu, 3, short)
    print(cat2.name, cat2.age, cat2.fur_length)


    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.fur_length)

    # create a car!
    car1 = Car(Highlander, 2016, Grey)
    # Now print out the function you made for car :)
    print(car1.model, car1.year, car1.color)

    main()
