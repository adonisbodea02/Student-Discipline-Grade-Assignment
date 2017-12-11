import sys
sys.path.append('/UBB/1st Year/FP/Assignment 5-7')
from Domain.Student import Student
from Domain.Exceptions import StudentException
import unittest


class StudentRepository:
    def __init__(self):
        '''
        creates an instance of the StudentRepository
        '''
        self.__data = []

    def __find(self, ID):
        '''
        returns the index Student having the given ID
        Input: ID - an integer, the ID of the student that is being searched
        Output: index - if the student was found, -1 otherwise
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getID() == ID:
                return i
        return -1

    def findBysID(self, ID):
        '''
            returns the index student having the given ID
            Input: ID - an integer, the ID of the student that is being searched
            Output: the student if it was found, none otherwise
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            return None
        return self.__data[indexID]

    def add(self, stu):
        '''
        add a Student to the repository
        Input: stu - object of type Student
        Output: the given student is added to the repository, if no other student has the same ID
        Exceptions: raises StudentException if another student with the same name already exists
        '''
        if self.findBysID(stu.getID()) != None:
            raise StudentException("Student with ID: " + str(stu.getID()) + " already exists!")
        self.__data.append(stu)

    def update(self, ID, newName):
        '''
        updates a student from the repository, using the given name
        Input - ID, a positive integer denoting the student that must be updated
              - newName, a string which will replace the name of the existing student
        Output - if such a student exists, the name is updated
        Exception - raises Exception if student with given ID does not exist
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise DisciplineException("There is no student with ID " + str(ID) + "!")
        self.__data[indexID].setName(newName)

    def remove(self, ID):
        '''
        removes a Student from the repository, using its name
        Input: ID, a positive integer denoting the Student that must be updated
        Output: if such a Discipline exists, it is removed
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise StudentException("There is no student with ID " + str(ID) + "!")
        self.__data.pop(indexID)

    def searchStringinName(self, string):
        '''
        searches a string in the name's of the students' repository
        Input: string
        Output: all the students in the repository that have the string in their names
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
        returns the size of the students list
        '''
        return len(self.__data)

    def getAll(self):
        '''
        returns the list of the students list
        '''
        return self.__data

class testStuRepo(unittest.TestCase):

    def testStudentRepository(self):
        repo = StudentRepository()

        s1 = Student(1, "Putin")
        s2 = Student(1, "Chandler")

        assert len(repo) == 0

        repo.add(s1)
        assert len(repo) == 1
        assert repo.findBysID(1) == s1

        assert repo.searchStringinName("ut") == [s1]
        assert repo.searchStringinName("ta") == []

        try:
            repo.add(s1)
            assert False
        except StudentException:
            assert True

        try:
            repo.add(s2)
            assert False
        except StudentException:
            assert True

        s2 = Student(2, "Chandler")
        repo.add(s2)
        assert len(repo) == 2
        assert repo.findBysID(1) == s1
        assert repo.findBysID(2) == s2

        repo.update(2, "Nonaka")

        repo.remove(1)
        assert len(repo) == 1
        assert repo.findBysID(2) == s2
        assert repo.findBysID(1) == None

        try:
            repo.remove(1)
            assert False
        except StudentException:
            assert True

        repo.remove(2)
        assert len(repo) == 0