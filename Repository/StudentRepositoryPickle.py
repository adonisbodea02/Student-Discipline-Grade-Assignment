import sys
sys.path.append('A:/UBB/1st Year/FP/Assignment 5-7')
import pickle
from Repository.StudentRepository import StudentRepository
from Domain.Student import Student
from Domain.Student import readStufromLine
from Domain.Student import writeStutoLine

class StudentRepositoryPickle(StudentRepository):

    def __init__(self, readStufromLine, writeStutoLine, fname):
        self._fname = fname
        StudentRepository.__init__(self)
        self._readStufromLine = readStufromLine
        self._writeStutoLine = writeStutoLine

    def readAllfromFile(self):

        with open(self._fname, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    stu = self._readStufromLine(line)
                    self.add(stu)
                except EOFError:
                    break

    def writeAlltoFile(self):

        with open(self._fname, 'wb') as f:

            for el in self.getAll():
                line = self._writeStutoLine(el)
                pickle.dump(line, f, pickle.HIGHEST_PROTOCOL)

            f.close()

# repoStudent = StudentRepositoryPickle(readStufromLine, writeStutoLine, 'Students.pickle')
# repoStudent.add(Student(1, "Mio Naruse"))
# repoStudent.add(Student(2, "Sheldon Cooper"))
# repoStudent.add(Student(3, "Joey Tribbiani"))
# repoStudent.add(Student(4, "Monica Bing"))
# repoStudent.writeAlltoFile()
# repoStudent.readAllfromFile()
# for i in repoStudent.getAll():
#     print(i)