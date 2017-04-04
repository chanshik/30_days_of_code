class Person(object):
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
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)

        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grades = [
            (90, 101, "O"),
            (80, 90, "E"),
            (70, 80, "A"),
            (55, 70, "P"),
            (40, 55, "D"),
            (0, 40, "T"),
        ]
        avg = sum(self.scores) / len(scores)

        for grade in grades:
            if grade[0] <= avg < grade[1]:
                return grade[2]


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )

    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()

    print("Grade:", s.calculate())
