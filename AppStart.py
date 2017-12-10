from Domain.Discipline import Discipline
from Domain.Discipline import readDisfromLine
from Domain.Discipline import writeDistoLine
from Domain.Grade import Grade
from Domain.Grade import readGrafromLine
from Domain.Grade import writeGratoLine
from Domain.Student import Student
from Domain.Student import readStufromLine
from Domain.Student import writeStutoLine
from Repository.DisciplineRepository import DisciplineRepository
from Repository.StudentRepository import StudentRepository
from Repository.GradeRepository import GradeRepository
from Repository.DisciplineRepositoryFile import DisciplineRepositoryFile
from Repository.StudentRepositoryFile import StudentRepositoryFile
from Repository.GradeRepositoryFile import GradeRepositoryFile
from Repository.DisciplineRepositoryPickle import DisciplineRepositoryPickle
from Repository.StudentRepositoryPickle import StudentRepositoryPickle
from Repository.GradeRepositoryPickle import GradeRepositoryPickle
from Controller.DisciplineController import DisciplineController
from Controller.StudentController import StudentController
from Controller.GradeController import GradeController
from Controller.StatisticsController import StatisticsController
from Controller.UndoController import UndoController
from UI.UI import UI
import sys
sys.path.append('/UBB/1st Year/FP/Assignment 5-7')

def repomode():

    f = open("settings.property.txt", "r")
    rep = f.readline().replace(' ', '')
    rep = rep.replace('"', '')
    rep = rep.strip('\n')
    rep = rep.split('=')
    stu = f.readline().replace(' ', '')
    stu = stu.replace('"', '')
    stu = stu.strip('\n')
    stu = stu.split('=')
    dis = f.readline().replace(' ', '')
    dis = dis.replace('"', '')
    dis = dis.strip('\n')
    dis = dis.split('=')
    gra = f.readline().replace(' ', '')
    gra = gra.replace('"', '')
    gra = gra.strip('\n')
    gra = gra.split('=')

    print(rep)
    print(stu)
    print(dis)
    print(gra)

    return rep[1], stu[1], dis[1], gra[1]


reads = repomode()

if reads[0] == "inmemory":

    repoDiscipline = DisciplineRepository()
    repoStudent = StudentRepository()
    repoGrade = GradeRepository()

elif reads[0] == "textfiles":

    repoDiscipline = DisciplineRepositoryFile(readDisfromLine, writeDistoLine)
    repoStudent = StudentRepositoryFile(readStufromLine, writeStutoLine)
    repoGrade = GradeRepositoryFile(readGrafromLine, writeGratoLine)

elif reads[0] == "binaryfiles":

    repoDiscipline = DisciplineRepositoryPickle(readDisfromLine, writeDistoLine, 'Disciplines.pickle')
    repoStudent = StudentRepositoryPickle(readStufromLine, writeStutoLine, 'Students.pickle')
    repoGrade = GradeRepositoryPickle(readGrafromLine, writeGratoLine, 'Grades.pickle')

repoDiscipline.add(Discipline(1, "How to draw manga"))
repoDiscipline.add(Discipline(2, "Japanese"))
repoDiscipline.add(Discipline(3, "Philosophy"))
repoDiscipline.add(Discipline(4, "Anime"))
repoDiscipline.add(Discipline(5, "Algebra"))
repoDiscipline.add(Discipline(6, "Introduction to Economics"))
repoDiscipline.add(Discipline(7, "Mathematical Analysis"))
repoDiscipline.add(Discipline(8, "Football"))
repoDiscipline.add(Discipline(9, "Table Tennis"))
repoDiscipline.add(Discipline(10, "Tennis"))
repoDiscipline.add(Discipline(11, "Introduction to Algorithms"))
repoDiscipline.add(Discipline(12, "Dragons Language"))
repoDiscipline.add(Discipline(13, "Introduction to How not to be a Social Outcast"))
repoDiscipline.add(Discipline(14, "Game Theory"))

repoStudent.add(Student(1, "Mio Naruse"))
repoStudent.add(Student(2, "Sheldon Cooper"))
repoStudent.add(Student(3, "Joey Tribbiani"))
repoStudent.add(Student(4, "Monica Bing"))
repoStudent.add(Student(5, "Chandler Bing"))
repoStudent.add(Student(6, "Natsu Dragneel"))
repoStudent.add(Student(7, "Akeno Himejima"))
repoStudent.add(Student(8, "Donald Trump"))
repoStudent.add(Student(9, "Friedrich Nietzsche"))
repoStudent.add(Student(10, "Immanuel Kant"))
repoStudent.add(Student(11, "Emmanuele Macron"))
repoStudent.add(Student(12, "Aine Chidorigafuchi"))
repoStudent.add(Student(13, "Sterling Archer"))
repoStudent.add(Student(14, "Kylian Mbappe Lottin"))
repoStudent.add(Student(15, "Ross Barkley"))
repoStudent.add(Student(16, "Adam Smith"))
repoStudent.add(Student(17, "Arthur Schopenhauer"))
repoStudent.add(Student(18, "Sherlock Holmes"))
repoStudent.add(Student(19, "Hercule Poirot"))
repoStudent.add(Student(20, "Marin Preda"))
repoStudent.add(Student(21, "Sasuke Uchiha"))
repoStudent.add(Student(22, "Itachi Uchiha"))
repoStudent.add(Student(23, "Light Yagami"))
repoStudent.add(Student(24, "Axl Rose"))
repoStudent.add(Student(25, "Harry Potter"))
repoStudent.add(Student(26, "Gottfried Wilhelm von Leibniz"))
repoStudent.add(Student(27, "Rene Descartes"))
repoStudent.add(Student(28, "Antoine Griezmann"))
repoStudent.add(Student(29, "Rafael Nadal"))
repoStudent.add(Student(30, "Barney Stinson"))
repoStudent.add(Student(31, "Lucy Heartfilia"))
repoStudent.add(Student(32, "Edward Elric"))
repoStudent.add(Student(33, "Erza Scarlet"))
repoStudent.add(Student(34, "Sena Kashiwazaki"))
repoStudent.add(Student(35, "Yusuke Urameshi"))
repoStudent.add(Student(36, "John von Neumann"))

repoGrade.addGrade(Grade(1, 1, 10), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(2, 12, 2.49), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(6, 33, 1.43), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 2, 7.89), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 34, 9.84), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 5, 6.22), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(14, 28, 7.6), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(8, 14, 7.62), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(8, 30, 6.7), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(10, 27, 5.1), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(4, 10, 7.91), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(8, 29, 7.78), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(11, 22, 9.69), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 5, 1.22), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(11, 6, 8.77), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(14, 11, 7.19), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(11, 35, 8.33), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 8, 4.45), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(1, 23, 7.8), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(6, 25, 8.36), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(8, 30, 1.34), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(5, 23, 2.71), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 32, 6.92), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(7, 29, 2.65), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(7, 20, 4.58), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(3, 9, 2.71), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 2, 5.56), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 27, 6.25), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(11, 7, 5.64), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 7, 5.13), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(4, 36, 4.41), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(3, 30, 5.49), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(5, 27, 7.36), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(1, 13, 3.1), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 3, 8.88), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(6, 19, 2.36), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(6, 36, 1.19), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(13, 3, 5.94), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(7, 18, 8.41), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(14, 18, 3.51), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(7, 11, 5.08), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(4, 26, 7.71), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 5, 2.03), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(7, 22, 7.86), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(9, 7, 3.79), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(4, 22, 5.88), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(10, 18, 9.59), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(5, 3, 1.63), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(2, 24, 4.64), repoStudent, repoDiscipline)
repoGrade.addGrade(Grade(2, 10, 4.97), repoStudent, repoDiscipline)

ctrlUndo = UndoController()
ctrlDiscipline = DisciplineController(repoDiscipline, repoGrade, repoStudent, ctrlUndo)
ctrlStudent = StudentController(repoStudent, repoGrade, repoDiscipline, ctrlUndo)
ctrlGrade = GradeController(repoGrade, repoDiscipline, repoStudent, ctrlUndo)
ctrlStatistics = StatisticsController(repoStudent, repoDiscipline, repoGrade)

ui = UI(ctrlDiscipline, ctrlStudent, ctrlGrade, ctrlStatistics, ctrlUndo)

ui.MainMenu()

if reads[0] == "textfiles":

    repoDiscipline.writeAlltoFile()
    repoStudent.writeAlltoFile()
    repoGrade.writeAlltoFile()

if reads[0] == "binaryfiles":

    repoDiscipline.writeAlltoFile()
    repoStudent.writeAlltoFile()
    repoGrade.writeAlltoFile()

