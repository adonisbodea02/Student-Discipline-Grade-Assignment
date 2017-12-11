from Domain.Student import Student
from Domain.Exceptions import StudentException
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Repository.DisciplineRepository import DisciplineRepository
from Controller.HistoryController import AddOperation, UpdateOperation, CascadeRemoveOperation
from Controller.UndoController import UndoController
from copy import deepcopy
import unittest

class StudentController:
    '''
    creates a new instance of Student Controller
    '''
    def __init__(self, stuRepo, graRepo, disRepo, undoCtrl):
        self.__repo = stuRepo
        self.__graRepo = graRepo
        self.__disRepo = disRepo

        self.__undoCtrl = undoCtrl
        self.__operations = []
        self.__index = 0

    def addStudent(self, stu):
        '''
        adds a Student to the register
        Input - stu - of type Student
        Output: the Student is added, if there is no other Student with the given ID
        Exceptions: raise StudentException if another Student with the same name already exists
        '''
        self.__operations = self.__operations[0:self.__index]

        self.__repo.add(stu)

        self.__operations.append(AddOperation(stu))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def updateStudent(self, ID, newName):
        '''
        updates a Student from the register, using the given ID
        Input: ID - positive integer, the ID of the Student be updated
               newName - the new name of the student
        Output: if such a Student exists, it is updated
        Exceptions: raises StudentException if a Student with the given ID does not exist
        '''
        self.__operations = self.__operations[0:self.__index]

        oldStudent = deepcopy(self.__repo.findBysID(ID))

        self.__repo.update(ID,newName)

        newStudent = deepcopy(self.__repo.findBysID(ID))

        self.__operations.append(UpdateOperation(oldStudent, newStudent))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def removeStudent(self, ID):
        '''
        removes a Student from the list, using its ID (it also removes the grades associated with the Student)
        Input: ID - positive integer, the ID of the Student to be removed
        Output: if such a Student exists, it is removed alongside with the grades associated with it
        Exception: raises a StudentException if a Student with the given ID does not exist
        '''
        self.__operations = self.__operations[0:self.__index]

        parent = self.__repo.findBysID(ID)
        affected = []

        SearchList = deepcopy(self.__graRepo.getAll())
        for gra in SearchList:
            if gra.getStudentID() == ID:
                affected.append(gra)
                self.__graRepo.removeGrade(gra.getDisciplineID(), gra.getStudentID())

        self.__repo.remove(ID)

        self.__operations.append(CascadeRemoveOperation(parent, affected))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def getAll(self):
        '''
        returns the list of Students
        '''
        return self.__repo.getAll()

    def searchStudentID(self, ID):
        '''
        searches for a Student based on the given ID
        Input: ID - positive integer , the ID of the Student that must be searched
        Output: if such a student exists, it is returned
        '''
        return self.__repo.findBysID(ID)

    def searchStringinNameStudent(self, string):
        '''
        searches a string in the name of the students' repository
        Input: string
        Output: all students that have the string in their names
        '''
        return self.__repo.searchStringinName(string)

    def __len__(self):
        '''
        returns the size of the list of students
        '''
        return len(self.__repo)

    def undo(self):
        '''
        undoes the last students operation that changed the list of students
        Returns True if the operation was successfully undone, False otherwise
        '''
        if self.__index == 0:
            return False

        self.__index -= 1
        operation = self.__operations[self.__index]

        if isinstance(operation, AddOperation):
            self.__repo.remove(operation.getObject().getID())
        elif isinstance(operation, CascadeRemoveOperation):
            parent = operation.Parent_Object
            affected = operation.Affected_Objects

            self.__repo.add(parent)
            for gra in affected:
                self.__graRepo.addGrade(gra, self.__repo, self.__disRepo)
        else:
            self.__repo.update(operation.getOldObject().getID(), operation.getOldObject().getName())

    def redo(self):
        '''
        redoes the last student operation that changed the list of students
        Returns True if operation was redone, False otherwise
        '''
        if self.__index == self.__len__() - 1:
            return False

        operation = self.__operations[self.__index]

        if isinstance(operation, AddOperation):
            self.__repo.add(operation.getObject())

        elif isinstance(operation, CascadeRemoveOperation):
            parent = operation.Parent_Object
            affected = operation.Affected_Objects

            self.__repo.remove(parent.getID())
            for gra in affected:
                self.__graRepo.removeGrade(gra.getDisciplineID(), gra.getStudentID())

        else:
            self.__repo.update(operation.getUpdatedObject().getID(), operation.getUpdatedObject().getName())

        self.__index += 1

class testStuController(unittest.TestCase):

    def testStudentController(self):
        stuRepo = StudentRepository()
        graRepo = GradeRepository()
        undoCtrl = UndoController()
        disRepo = DisciplineRepository()
        ctrl = StudentController(stuRepo, graRepo, disRepo, undoCtrl)

        s1 = Student(1, "Putin")
        s2 = Student(1, "Boruto")

        assert len(ctrl) == 0

        ctrl.addStudent(s1)
        assert len(ctrl) == 1
        assert ctrl.searchStudentID(1) == s1

        try:
            ctrl.addStudent(s1)
            assert False
        except StudentException:
            assert True

        try:
            ctrl.addStudent(s2)
            assert False
        except StudentException:
            assert True

        s2 = Student(2, "Naruse")
        ctrl.addStudent(s2)
        assert len(ctrl) == 2
        assert ctrl.searchStringinNameStudent("TIN") == [s1]
        assert ctrl.searchStringinNameStudent("rus") == [s2]

        ctrl.updateStudent(1,"Hagi")

        assert len(ctrl) == 2
        ctrl.removeStudent(1)
        assert len(ctrl) == 1
        assert ctrl.searchStudentID(1) == None
        assert ctrl.searchStudentID(2) == s2

        try:
            ctrl.removeStudent(1)
            assert False
        except StudentException:
            assert True

        ctrl.removeStudent(2)
        assert len(ctrl) == 0

