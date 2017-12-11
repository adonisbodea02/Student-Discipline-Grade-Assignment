from Domain.Grade import Grade
from Domain.Student import Student
from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Repository.DisciplineRepository import DisciplineRepository
from copy import deepcopy
from operator import itemgetter
import unittest


class StatisticsController:

    def __init__(self, stuRepo, disRepo, graRepo):

        self.__stuRepo = stuRepo
        self.__graRepo = graRepo
        self.__disRepo = disRepo

    def byDisciplineAlphabetically(self, ID):
        """
        creates a statistic for a given discipline
        Input: ID - positive integer
        Ouput: a list containing all the student at a given discipline
        Exception: raises DisciplineException if the given ID does not match a Discipline in the Discipline Repository
        """
        disalpha = []
        if self.__disRepo.findBydID(ID) != None:
            for gra in self.__graRepo.getAll():
                if gra.getDisciplineID() == ID:
                    stu = self.__stuRepo.findBysID(gra.getStudentID())
                    ID1 = stu.getID()
                    name = stu.getName()
                    v = [ID1, name]
                    t = False
                    for i in range(len(disalpha)):
                        if disalpha[i][0] == ID1:
                            t = True
                    if t == False:
                        disalpha.append(v)
        else:
            raise DisciplineException("Discipline with ID " + str(ID) + " does not exist!")

        disalpha.sort(key=itemgetter(1))
        return disalpha

    def failingStudents(self):
        """
        creates a statistic with the failing students at one or more disciplines
        Input: none
        Output: a list containing all failing students
        """
        failStu = []
        for stu in self.__stuRepo.getAll():
            for dis in self.__disRepo.getAll():
                nr = 0
                avg = 0
                for gra in self.__graRepo.getAll():
                    if stu.getID() == gra.getStudentID() and dis.getID() == gra.getDisciplineID():
                        avg = avg + gra.getGrade()
                        nr += 1
                if nr > 0:
                    avg = avg/nr
                    if avg < 5:
                        ID = stu.getID()
                        name = stu.getName()
                        v = [ID, name]
                        t = False
                        for i in range(len(failStu)):
                            if failStu[i][0] == ID:
                                t = True
                        if t == False:
                            failStu.append(v)
        return failStu

    def topStudents(self):
        """
        creates a statistic with the best students sorted by their average of averages
        Input: none
        Output: a list containing the top students sorted accordingly
        """
        topStu = []
        for stu in self.__stuRepo.getAll():
            contor1 = 0
            avg1 = 0
            for dis in self.__disRepo.getAll():
                contor2 = 0
                avg2 = 0
                for gra in self.__graRepo.getAll():
                    if stu.getID() == gra.getStudentID() and dis.getID() == gra.getDisciplineID():
                        avg2 = avg2 + gra.getGrade()
                        contor2 += 1
                if contor2 > 0:
                    avg2 = avg2/contor2
                    avg1 = avg1 + avg2
                    contor1 += 1
            if contor1 > 0:
                avg1 = avg1/contor1
                ID = stu.getID()
                name = stu.getName()
                v = [avg1, ID, name]
                topStu.append(v)
        topStu.sort(key=itemgetter(0), reverse=True)
        return topStu

    def topDiscipline(self):
        """
        creates a statistic with all the disciplines sorted based on the average of grades at each one
        Input: none
        Output: a list with the disciplines sorted accordingly
        """
        topDis = []
        for dis in self.__disRepo.getAll():
            contor = 0
            avg = 0
            for gra in self.__graRepo.getAll():
                if dis.getID() == gra.getDisciplineID():
                    avg = avg + gra.getGrade()
                    contor += 1
            if contor > 0:
                avg = avg/contor
                ID = dis.getID()
                name = dis.getName()
                v = [avg, ID, name]
                topDis.append(v)
        topDis.sort(key=itemgetter(0), reverse=True)
        return topDis

class testStaController(unittest.TestCase):

    def testStatisticsController(self):

        graRepo = GradeRepository()
        stuRepo = StudentRepository()
        disRepo = DisciplineRepository()

        disRepo.add(Discipline(1, "Dragons Language"))
        disRepo.add(Discipline(2, "How to draw anime"))
        disRepo.add(Discipline(3, "Japanese"))

        stuRepo.add(Student(1, "Putin"))
        stuRepo.add(Student(2, "Sheldon Cooper"))
        stuRepo.add(Student(3, "Nietzsche"))
        stuRepo.add(Student(4, "Mio Naruse"))

        graRepo.addGrade(Grade(1, 1, 9.9), stuRepo, disRepo)
        graRepo.addGrade(Grade(2, 1, 4.8), stuRepo, disRepo)
        graRepo.addGrade(Grade(3, 1, 5.7), stuRepo, disRepo)
        graRepo.addGrade(Grade(2, 2, 9.0), stuRepo, disRepo)
        graRepo.addGrade(Grade(1, 3, 6.0), stuRepo, disRepo)
        graRepo.addGrade(Grade(2, 3, 7.3), stuRepo, disRepo)
        graRepo.addGrade(Grade(3, 3, 4.2), stuRepo, disRepo)
        graRepo.addGrade(Grade(3, 3, 7.9), stuRepo, disRepo)

        ctrl = StatisticsController(stuRepo, disRepo, graRepo)

        assert ctrl.byDisciplineAlphabetically(3) == [[3, 'Nietzsche'], [1, 'Putin']]
        assert ctrl.byDisciplineAlphabetically(2) == [[3, 'Nietzsche'], [1, 'Putin'], [2, 'Sheldon Cooper']]
        assert ctrl.failingStudents() == [[1, 'Putin']]
        assert ctrl.topStudents() == [[9.0, 2, 'Sheldon Cooper'], [6.8, 1, 'Putin'], [6.45, 3, 'Nietzsche']]
        assert ctrl.topDiscipline() == [[7.95, 1, 'Dragons Language'], [7.033333333333334, 2, 'How to draw anime'], [5.933333333333334, 3, 'Japanese']]
