from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
import unittest


class DisciplineRepository:
    def __init__(self):
        '''
        creates an instance of the DisciplineRepository
        '''
        self.__data = []

    def __find(self, ID):
        '''
        returns the index Discipline having the given ID
        Input: ID - an integer, the ID of the discipline that is being searched
        Output: index - if the discipline was found, -1 otherwise
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getID() == ID:
                return i
        return -1

    def findBydID(self, ID):
        '''
            returns the index Discipline having the given ID
            Input: ID - an integer, the ID of the discipline that is being searched
            Output: the discipline if it was found, none otherwise
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            return None
        return self.__data[indexID]

    def add(self, dis):
        '''
        add a Discipline to the repository
        Input: dis - object of type Discipline
        Output: the given Discipline is added to the repository, if no other Discipline has the same ID
        Exceptions: raises DisciplineException if another Discipline with the same name already exists
        '''
        if self.findBydID(dis.getID()) != None:
            raise DisciplineException("Discipline with ID " + str(dis.getID()) + " already exists!")
        self.__data.append(dis)

    def update(self, ID, newName):
        '''
        updates a Discipline from the repository, using the given name
        Input - ID, a positive integer denoting the Discipline that must be updated
              - newName, a string which will replace the name of the existing Discipline
        Output - if such a Discipline exists, the name is updated
        Exception - raises Exception if Discipline with given ID does not exist
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise DisciplineException("There is no discipline with ID " + str(ID) + "!")
        self.__data[indexID].setName(newName)

    def remove(self, ID):
        '''
        removes a Discipline from the repository, using its name
        Input: ID, a positive integer denoting the Discipline that must be updated
        Output: if such a Discipline exists, it is removed
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise DisciplineException("There is no discipline with ID " + str(ID) + "!")
        self.__data.pop(indexID)

    def searchStringinName(self, string):
        '''
        searches a string in the name's of the disciplines' repository
        Input: string
        Output: all the Disciplines in the repository that have the string in their names
        '''
        res = []
        for i in range(len(self.__data)):
            Name = self.__data[i].getName()
            Name = Name.upper()
            if Name.find(string.upper()) != -1:
                res.append(self.__data[i])
        return res

    def __len__ (self):
        '''
        returns the size of the disciplines list
        '''
        return len(self.__data)

    def getAll(self):
        '''
        returns the list of the disciplines list
        '''
        return self.__data

class testDisRepo(unittest.TestCase):

    def testDisciplineRepository(self):
        repo = DisciplineRepository()

        d1 = Discipline(1, "Japanese")
        d2 = Discipline(1, "How to draw anime")

        assert len(repo) == 0

        repo.add(d1)
        assert len(repo) == 1
        assert repo.findBydID(1) == d1

        assert repo.searchStringinName("AP") == [d1]
        assert repo.searchStringinName("ta") == []

        try:
            repo.add(d1)
            assert False
        except DisciplineException:
            assert True

        try:
            repo.add(d2)
            assert False
        except DisciplineException:
            assert True

        d2 = Discipline(2, "How to draw anime")
        repo.add(d2)
        assert len(repo) == 2
        assert repo.findBydID(1) == d1
        assert repo.findBydID(2) == d2

        repo.update(2, "Anime")

        repo.remove(1)
        assert len(repo) == 1
        assert repo.findBydID(2) == d2
        assert repo.findBydID(1) == None

        try:
            repo.remove(1)
            assert False
        except DisciplineException:
            assert True

        repo.remove(2)
        assert len(repo) == 0