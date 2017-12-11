import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
from Repository.GradeRepository import GradeRepository
from Domain.Grade import Grade
from Domain.Grade import readGrafromLine
from Domain.Grade import writeGratoLine

class GradeRepositoryFile(GradeRepository):

    def __init__(self, readGrafromLine, writeGratoLine, fname = "Grades.txt"):
        self._fname = fname
        GradeRepository.__init__(self)
        self._readGrafromLine = readGrafromLine
        self._writeGratoLine = writeGratoLine

    def readAllfromFile(self):
        """
        reads all data from the Grades file
        returns a list of data from the Grades file
        """
        with open(self._fname, 'r') as f:
            lines = f.readlines()
            readList = []
            for line in lines:
                line = line.strip()
                if len(line) > 1:
                    gra = self._readGrafromLine(line)
                    readList.append(gra)
            f.close()
            return readList

    def writeAlltoFile(self):
        """
        writes all data to the Grades File
        returns: none
        """
        with open(self._fname, 'w') as f:
            for elem in self.getAll():
                line = self._writeGratoLine(elem)
                f.write(line + "\n")
            f.close()

repo = GradeRepositoryFile(readGrafromLine, writeGratoLine)
