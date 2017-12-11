from Domain.Grade import Grade
from Domain.Discipline import Discipline
from Domain.Student import Student
from Repository.DisciplineRepository import DisciplineRepository
from Repository.StudentRepository import StudentRepository
from Domain.Exceptions import GradeException
import unittest

class GradeRepository:
    def __init__(self):
        '''
        creates an instance of grade Repository
        '''
        self.__data = []

    def __find(self, DisciplineID, StudentID):
        '''
        returns the index of the grade having the given studentID and disciplineID
        Input: StudentID - positive integer
               DisciplineID - positive integer
        Output: index - if the grade was found
                -1 - otherwise
        '''
        for i in range (len(self.__data)):
            if self.__data[i].getDisciplineID() == DisciplineID and self.__data[i].getStudentID() == StudentID:
                return i
        return -1

    def addGrade(self, gra, sturepo, disrepo):
        '''
        adds a grade to the grade repository
        Input: gra - object type of grade
        Output: the given grade is added to the repository, if the studentID and disciplineID of the grade exists
        Exception: the disID or the stuID does not exist
        '''
        if disrepo.findBydID(gra.getDisciplineID()) != None and sturepo.findBysID(gra.getStudentID()) != None:
            self.__data.append(gra)
        else:
            #print(sturepo.findBysID(gra.getStudentID()))
            raise GradeException("Student with ID: " + str(gra.getStudentID()) + " or the discipline with ID: " + str(gra.getDisciplineID()) + " does not exist!")

    def removeGrade(self, disID, stuID):
        '''
        removes a grade with the given student ID and discipline ID
        Input: disID - positive integer, the ID of the grade's discipline to be removed
               stuID - positive integer, the ID of the grade's student to be removed
        Output: if such a Grade exists, it is removed and returned
        Exceptions: raises GradeException if a Grade with the given disID and stuID does not exist
        '''
        indexDisciplineIDandStudentID = self.__find(disID, stuID)
        if indexDisciplineIDandStudentID == -1:
            raise GradeException("There is no grade with the student ID: " + str(stuID) + " and discipline ID: " + str(disID) + "!")

        self.__data.pop(indexDisciplineIDandStudentID)

    def __len__(self):
        '''
        returns the size of the list of grades
        '''
        return len(self.__data)

    def getAll(self):
        '''
        returns the list of grades
        '''
        return self.__data

class testGradeRepo(unittest.TestCase):

    def testGradeRepository(self):

        repo = GradeRepository()
        disrepo = DisciplineRepository()
        sturepo = StudentRepository()

        stu = Student(1, "Putin")
        dis = Discipline(1, "Maths")

        sturepo.add(stu)
        disrepo.add(dis)

        assert len(repo) == 0

        gra1 = Grade(1, 1, 10)

        repo.addGrade(gra1, sturepo, disrepo)

        assert len(repo) == 1

        repo.removeGrade(1,1)

        assert len(repo) == 0

        try:
            repo.removeGrade(1,1)
            assert False
        except GradeException:
            assert True
