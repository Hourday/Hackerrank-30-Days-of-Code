class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName,idNumber,scores):    
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores =scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    
    def calculate(self):
        y=0
        grade=""
        for x in scores:
            y=y+x 
        y=y/len(scores)
        if y>=90 and y<=100:
            grade="O"
        elif y>=80 and y<90:
            grade="E"
        elif y>=70 and y<80:
            grade="A"
        elif y>=55 and y<70:
            grade="P"
        elif y>=40 and y<55:
            grade="D"
        #elif y>40:    
        else:    
            grade="T"
        return(grade)

line = input().split()