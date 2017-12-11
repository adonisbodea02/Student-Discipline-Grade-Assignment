from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
from Repository.DisciplineRepository import DisciplineRepository
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Controller.HistoryController import AddOperation, UpdateOperation, CascadeRemoveOperation
from Controller.UndoController import UndoController
from copy import deepcopy
import unittest

class DisciplineController:
    '''
    creates a new instance of Discipline Controller
    '''
    def __init__(self, disRepo, graRepo, stuRepo, undoCtrl):
        self.__repo = disRepo
        self.__graRepo = graRepo
        self.__stuRepo = stuRepo

        self.__undoCtrl = undoCtrl
        self.__operations = []
        self.__index = 0

    def addDiscipline(self, dis):
        '''
        adds a Discipline to the register
        Input - dis - of type Discipline
        Output: the Discipline is added, if there is no other Discipline with the given ID
        Exceptions: raise DisciplineException if another Discipline with the same name already exists
        '''
        self.__operations = self.__operations[0:self.__index]

        self.__repo.add(dis)

        self.__operations.append(AddOperation(dis))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def updateDiscipline(self, ID, newName):
        '''
        updates a Discipline from the register, using the given ID
        Input: ID - positive integer, the ID of the Discipline to be updated
               newName - the new name of the discipline
        Output: if such a Discipline exists, it is updated
        Exceptions: raises DisciplineException if a Discipline with the given ID does not exists
        '''
        self.__operations = self.__operations[0:self.__index]

        oldDiscipline = deepcopy(self.__repo.findBydID(ID))

        self.__repo.update(ID, newName)

        newDiscipline = deepcopy(self.__repo.findBydID(ID))

        self.__operations.append(UpdateOperation(oldDiscipline, newDiscipline))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def removeDiscipline(self, ID):
        '''
        removes a Discipline from the list, using its ID (it also removes the grades associated with the Discipline)
        Input: ID - positive integer, the ID of the Discipline to be removed
        Output: if such a Discipline exists, it is removed alongside with the grades associated with it
        Exception: raises a DisciplineException if a Discipline with the given ID does not exist
        '''
        self.__operations = self.__operations[0:self.__index]

        parent = self.__repo.findBydID(ID)
        affected = []

        SearchList = deepcopy(self.__graRepo.getAll())
        for gra in SearchList:
            if gra.getDisciplineID() == ID:
                affected.append(gra)
                self.__graRepo.removeGrade(gra.getDisciplineID(), gra.getStudentID())

        self.__repo.remove(ID)

        self.__operations.append(CascadeRemoveOperation(parent, affected))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])

    def getAll(self):
        '''
        returns the list of disciplines
        '''
        return self.__repo.getAll()

    def searchDisciplineID(self, ID):
        '''
        searches for a Discipline based on the given ID
        Input: ID - positive integer , the ID of the Discipline that must be searched
        Output: if such a discipline exists, it is returned
        '''
        return self.__repo.findBydID(ID)

    def searchStringinNameDiscipline(self, string):
        '''
        searches a string in the name of the disciplines' repository
        Input: string
        Output: all disciplines that have the string in their names
        '''
        return self.__repo.searchStringinName(string)

    def __len__(self):
        '''
        returns the size of the list of disciplines
        '''
        return len(self.__repo)

    def undo(self):
        '''
        undoes the last discipline operation that changed the list of disciplines
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
                self.__graRepo.addGrade(gra, self.__stuRepo, self.__repo)
        else:
            self.__repo.update(operation.getOldObject().getID(), operation.getOldObject().getName())

    def redo(self):
        '''
        redoes the last discipline operation that changed the list of disciplines
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

class testDisController(unittest.TestCase):

    def testDisciplineController(self):
        disRepo = DisciplineRepository()
        graRepo = GradeRepository()
        stuRepo = StudentRepository()
        undoCtrl = UndoController()
        ctrl = DisciplineController(disRepo, graRepo, stuRepo, undoCtrl)

        d1 = Discipline(1, "Japanese")
        d2 = Discipline(1, "Anime")

        assert len(ctrl) == 0

        ctrl.addDiscipline(d1)
        assert len(ctrl) == 1
        assert ctrl.searchDisciplineID(1) == d1

        try:
            ctrl.addDiscipline(d1)
            assert False
        except DisciplineException:
            assert True

        try:
            ctrl.addDiscipline(d2)
            assert False
        except DisciplineException:
            assert True

        d2 = Discipline(2, "Manga")
        ctrl.addDiscipline(d2)
        assert len(ctrl) == 2
        assert ctrl.searchStringinNameDiscipline("ANG") == [d2]
        assert ctrl.searchStringinNameDiscipline("nes") == [d1]

        ctrl.updateDiscipline(1,"Anime")
        assert ctrl.searchStringinNameDiscipline("nim") == [d1]

        assert len(ctrl) == 2
        ctrl.removeDiscipline(1)
        assert len(ctrl) == 1
        assert ctrl.searchDisciplineID(1) == None
        assert ctrl.searchDisciplineID(2) == d2

        try:
            ctrl.removeDiscipline(1)
            assert False
        except DisciplineException:
            assert True

        ctrl.removeDiscipline(2)
        assert len(ctrl) == 0


