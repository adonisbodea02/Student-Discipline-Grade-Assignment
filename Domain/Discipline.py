import unittest

class Discipline:
    def __init__(self, ID, name):
        '''
        creates a new instance of Discipline
        '''
        self.__ID = ID
        self.__name = name

    def getID(self):
        '''
        getter for the ID of the Discipline
        '''
        return self.__ID

    def getName(self):
        '''
        getter for the ID of the Discipline
        '''
        return self.__name

    def setName(self, name):
        '''
        setter for the name of the Discipline
        '''
        self.__name = name

    def __str__(self):
        return "ID: " + str(self.__ID) + " Name: " + self.__name

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.getName() == other.getName() and \
            self.getID() == other.getID()

def readDisfromLine(line):
    line = line.split(";")
    ID = int(line[0])
    name = line[1]
    dis = Discipline(ID, name)
    return dis

def writeDistoLine(elem):
    string = str(elem.getID()) + ";" + elem.getName()
    return string

class testDis(unittest.TestCase):
    def testDis(self):
        dis = Discipline(1, "Japanese")
        assert dis.getID() == 1
        assert dis.getName() == "Japanese"
        dis.setName("Maths")
        assert dis.getName() == "Maths"

