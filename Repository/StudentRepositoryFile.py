import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
from Repository.StudentRepository import StudentRepository
from Domain.Student import Student
from Domain.Student import readStufromLine
from Domain.Student import writeStutoLine

class StudentRepositoryFile(StudentRepository):

    def __init__(self, readStufromLine, writeStutoLine, fname = "Students.txt"):
        self._fname = fname
        StudentRepository.__init__(self)
        self._readStufromLine = readStufromLine
        self._writeStutoLine = writeStutoLine

    def readAllfromFile(self):
        """
        reads all data from the Student file
        returns a list of data from the Student file
        """
        with open(self._fname, 'r') as f:
            lines = f.readlines()
            readList = []
            for line in lines:
                line = line.strip()
                if len(line) > 1:
                    stu = self._readStufromLine(line)
                    readList.append(stu)
            f.close()
            return readList

    def writeAlltoFile(self):
        """
        writes all data to the Student File
        returns: none
        """
        with open(self._fname, 'w') as f:
            for elem in self.getAll():
                line = self._writeStutoLine(elem)
                f.write(line + "\n")
            f.close()

repo = StudentRepositoryFile(readStufromLine, writeStutoLine)



