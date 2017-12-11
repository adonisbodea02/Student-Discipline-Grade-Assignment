import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
import pickle
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Repository.DisciplineRepository import DisciplineRepository
from Domain.Student import Student
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.Grade import readGrafromLine
from Domain.Grade import writeGratoLine

class GradeRepositoryPickle(GradeRepository):

    def __init__(self, readGrafromLine, writeGratoLine, fname):
        self._fname = fname
        GradeRepository.__init__(self)
        self._readGrafromLine = readGrafromLine
        self._writeGratoLine = writeGratoLine

    def readAllfromFile(self, stuRepo, disRepo):

        with open(self._fname, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    gra = self._readGrafromLine(line)

                    self.addGrade(gra, stuRepo, disRepo)
                except EOFError:
                    break

    def writeAlltoFile(self):

        with open(self._fname, 'wb') as f:

            for el in self.getAll():
                line = self._writeGratoLine(el)
                pickle.dump(line, f, pickle.HIGHEST_PROTOCOL)

            f.close()



