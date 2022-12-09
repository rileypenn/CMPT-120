# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day.
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''


class student:
    def __init__(self, name, studentId, year, major, gpa):
        #name
        self.name = name
        #studentId
        self.studentId = studentId
        #year
        self.year = year
        #major
        self.major = major
        #gpa
        self.gpa = gpa

import random

def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)


def main():

# create a function to see if the student is eligible for the honors program
    def honorsAcceptance(self):
        # to be eligible they need to have a gpa above 3.5
        # return true if they can and false if they cant, and print it out
        if gpa > 3.5:
            return true
            print("Congrats, you are accepted!")
        else:
            return false
            print("Sorry, you are rejected")

    #create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day.
    def freeLunch(self):
        #1. generate a random number the length of however long you choose to make the id number
        generatedStudentId = randN(8)
        print(generatedStudentId)

# create three students and check if they get free lunch and if they qualify for honors
    student1 = Student(Cally, 20495867, 2001, arts, 3.6)
    student2 = Student(Michael, 10389246, 2002, buisness, 2.9)
    student3 = Student(Terek, 69306872, 2000, math, 3.8)

    if freeLunch() == student1:
        print("Congrats student 1!")
        
    elif freeLunch() == student2:
        print("Congrats student 2")
        
    elif freeLunch() == student3:
        print("Congrats student 3")
        
    else:
        print("No free lunch :(")
    

main()
