import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
import pickle
from Repository.DisciplineRepository import DisciplineRepository
from Domain.Discipline import Discipline
from Domain.Discipline import readDisfromLine
from Domain.Discipline import writeDistoLine

class DisciplineRepositoryPickle(DisciplineRepository):

    def __init__(self, readDisfromLine, writeDistoLine, fname):
        self._fname = fname
        DisciplineRepository.__init__(self)
        self._readDisfromLine = readDisfromLine
        self._writeDistoLine = writeDistoLine

    def readAllfromFile(self):

        with open(self._fname, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    dis = self._readDisfromLine(line)
                    self.add(dis)
                except EOFError:
                    break

    def writeAlltoFile(self):

        with open(self._fname, 'wb') as f:

            for el in self.getAll():
                line = self._writeDistoLine(el)
                pickle.dump(line, f, pickle.HIGHEST_PROTOCOL)

            f.close()

# repoDiscipline = DisciplineRepositoryPickle(readDisfromLine, writeDistoLine, 'Discipline.pickle')
# repoDiscipline.readAllfromFile()
# for i in repoDiscipline.getAll():
#     print(i)