import unittest

class Grade:
    def __init__(self, disciplineID, studentID, grade):
        '''
        creates a new instance of Grade
        '''
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__grade = grade

    def getDisciplineID(self):
        '''
        getter for the grade's ID of the Discipline
        '''
        return self.__disciplineID

    def getStudentID(self):
        '''
        getter for grade's ID of the Student
        '''
        return self.__studentID

    def getGrade(self):
        '''
        getter for the grade's value
        '''
        return self.__grade

    def __str__(self):
        return "Discipline ID: " + str(self.__disciplineID) + " Student ID: " + str(self.__studentID) + " Mark: " + str(self.__grade)

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.getDisciplineID() == other.getDisciplineID() and \
            self.getStudentID() == other.getStudentID() and \
            self.getGrade() == other.getGrade()

def readGrafromLine(line):
    line = line.split(";")
    disID = int(line[0])
    stuID = int(line[1])
    grade = float(line[2])
    gra = Grade(disID, stuID, grade)
    return gra

def writeGratoLine(elem):
    string = str(elem.getDisciplineID()) + ";" + str(elem.getStudentID()) + ";" + str(elem.getGrade())
    return string

class testGra(unittest.TestCase):
    def testGra(self):
        grade = Grade(1, 2, 8)
        assert grade.getDisciplineID() == 1
        assert grade.getStudentID() == 2
        assert grade.getGrade() == 8


