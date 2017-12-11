import unittest

class Student:

    def __init__(self, ID, name):
        '''
        creates a new instance of Student
        '''
        self.__ID = ID
        self.__name = name

    def getID(self):
        '''
        getter for the ID of the Student
        '''
        return self.__ID

    def getName(self):
        '''
        getter for the ID of the Student
        '''
        return  self.__name

    def setName(self, name):
        '''
        setter for the name of the Student
        '''
        self.__name = name

    def __str__(self):
        return "ID: " + str(self.__ID) + " Name: " + self.__name

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.getName() == other.getName() and \
            self.getID() == other.getID()

def readStufromLine(line):
    line = line.split(";")
    ID = int(line[0])
    name = line[1]
    stu = Student(ID, name)
    return stu

def writeStutoLine(elem):
    string = str(elem.getID()) + ";" + elem.getName()
    return string

class testStu(unittest.TestCase):

    def testStu(self):
        student = Student(1, "Mio Naruse")
        assert student.getID() == 1
        assert student.getName() == "Mio Naruse"
        student.setName("Natsu")
        assert student.getName() == "Natsu"
