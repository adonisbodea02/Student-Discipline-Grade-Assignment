from Domain.Grade import Grade
from Domain.Exceptions import GradeException
from Domain.Student import Student
from Domain.Exceptions import StudentException
from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Repository.DisciplineRepository import DisciplineRepository
from Controller.HistoryController import AddOperation, UpdateOperation, CascadeRemoveOperation
from Controller.UndoController import UndoController
from copy import deepcopy
import unittest


class GradeController:
    '''
    creates a new instance of grade controller
    '''
    def __init__(self, graRepo, disRepo, stuRepo, undoCtrl):
        self.__repo = graRepo
        self.__disRepo = disRepo
        self.__stuRepo = stuRepo

        self.__undoCtrl = undoCtrl
        self.__operations = []
        self.__index = 0

    def addGrade(self, grade):
        '''
        adds a grade to the lists of grade
        Input: grade - object of type grade
        Output: the given grade is added, if the given grade is valid
        Exceptions: raises DisciplineExceptions if the given discipline's name does not exist in the Discipline list
                    raises StudentExceptions if the given student's name does not exist in the Student list
        '''
        self.__operations = self.__operations[0:self.__index]

        if self.__disRepo.findBydID(grade.getDisciplineID()) == None:
            raise DisciplineException("There is no discipline with ID " + str(grade.getDisciplineID()) + "!")
        if self.__stuRepo.findBysID(grade.getStudentID()) == None:
            raise StudentException("There is no student with ID " + str(grade.getStudentID()) + "!")

        self.__repo.addGrade(grade, self.__stuRepo, self.__disRepo)

        self.__operations.append(AddOperation(grade))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def getAll(self):
        """
        returns the list of Grades
        """
        return self.__repo.getAll()

    def __len__(self):
        """
        returns the length of the list of grades
        """
        return len(self.__repo)

    def undo(self):
        """
        undoes the last Grade operation that changed the list of grades
        Returns true if the operation was successful, False otherwise
        """
        if self.__index == 0:
            return False

        self.__index -=1
        operation = self.__operations[self.__index]

        if isinstance(operation, AddOperation):
            self.__repo.removeGrade(operation.getObject().getDisciplineID(), operation.getObject().getStudentID())

    def redo(self):
        """
        redoes the last operation that changed the list of grades
        returns true if the operation was redone, False otherwise
        """
        if self.__index == self.__len__() - 1:
            return False

        operation = self.__operations[self.__index]

        if isinstance(operation, AddOperation):
            self.__repo.add(operation.getObject(), self.__stuRepo, self.__disRepo)

        self.__index += 1


class testGraController(unittest.TestCase):

    def testGradeController(self):

        graRepo = GradeRepository()
        disRepo = DisciplineRepository()
        stuRepo = StudentRepository()
        undoCtrl = UndoController()
        ctrl = GradeController(graRepo, disRepo, stuRepo, undoCtrl)

        assert len(ctrl) == 0
        grade = Grade(1, 1, 9)

        try:
            ctrl.addGrade(grade)
            assert False
        except (DisciplineException, StudentException):
            assert True

        d = Discipline(1, "Japanese")
        s = Student(1, "Naruto")
        disRepo.add(d)
        stuRepo.add(s)

        ctrl.addGrade(grade)

        assert len(ctrl) == 1
