import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
from Repository.DisciplineRepository import DisciplineRepository
from Domain.Discipline import Discipline
from Domain.Discipline import readDisfromLine
from Domain.Discipline import writeDistoLine

class DisciplineRepositoryFile(DisciplineRepository):

    def __init__(self, readDisfromLine, writeDistoLine, fname = 'Disciplines.txt'):
        self._fname = fname
        DisciplineRepository.__init__(self)
        self._readDisfromLine = readDisfromLine
        self._writeDistoLine = writeDistoLine

    def readAllfromFile(self):
        """
        reads all data from the Discipline file
        returns a list of data from the Discipline file
        """
        with open(self._fname, 'r') as f:
            lines = f.readlines()
            readList = []
            for line in lines:
                line = line.strip()
                if len(line) > 1:
                    dis = self._readDisfromLine(line)
                    readList.append(dis)
            f.close()
            return readList

    def writeAlltoFile(self):
        """
        writes all data to the Discipline File
        returns: none
        """
        with open(self._fname, 'w') as f:
            for elem in self.getAll():
                line = self._writeDistoLine(elem)
                f.write(line + "\n")
            f.close()

repo = DisciplineRepositoryFile(readDisfromLine, writeDistoLine)
