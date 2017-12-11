import sys
sys.path.append('/UBB/1st Year/FP/Assignment 5-7')
from Domain.Discipline import Discipline
from Domain.Student import Student
from Domain.Grade import Grade
from Domain.Exceptions import DisciplineException, StudentException, GradeException

class UI:
    def __init__(self, disController, stuController, graController, staController, undoController):
        self.__disCtrl = disController
        self.__stuCtrl = stuController
        self.__graCtrl = graController
        self.__staCtrl = staController
        self.__undoCtrl = undoController

    @staticmethod
    def printMenu():
        string = 'Available commands:\n'
        string += '\t 1. Manage disciplines \n'
        string += '\t 2. Manage students \n'
        string += '\t 3. Manage grades \n'
        string += '\t 4. Display statistics \n'
        string += '\t 5. Undo the last operation \n'
        string += '\t 6. Redo the last operation \n'
        string += '\t 0. Exit \n'
        print(string)

    @staticmethod
    def ValidInputCommand(command):
        """
        checks if the given command is a valid one
        Input: command - the given command - string
        Output: True - if the command is a valid ID command
                False - otherwise
        """
        availableCommands = ['1', '2', '3', '4', '5', '6', '0']
        return (command in availableCommands)

    @staticmethod
    def printDisciplineMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1. Add a discipline \n'
        string += '\t 2. Update a discipline \n'
        string += '\t 3. Remove a discipline \n'
        string += '\t 4. Search a discipline by ID \n'
        string += '\t 5. Search disciplines by name \n'
        string += '\t 6. Display all disciplines \n'
        string += '\t 0. Back to main menu \n'
        print(string)

    @staticmethod
    def validDisciplineCommand(command):
        """
            checks if the given command is a valid one
            Input: command - the given command - string
            Output: True - if the command is a valid ID command
                    False - otherwise
            """
        availableCommands = ['1', '2', '3', '4', '5', '6', '0']
        return (command in availableCommands)

    @staticmethod
    def printStudentMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1. Add a student \n'
        string += '\t 2. Update a student \n'
        string += '\t 3. Remove a student \n'
        string += '\t 4. Search a student by ID \n'
        string += '\t 5. Search student by name \n'
        string += '\t 6. Display all students \n'
        string += '\t 0. Back to main menu \n'
        print(string)

    @staticmethod
    def validStudentCommand(command):
        """
            checks if the given command is a valid one
            Input: command - the given command - string
            Output: True - if the command is a valid ID command
                    False - otherwise
            """
        availableCommands = ['1', '2', '3', '4', '5', '6', '0']
        return (command in availableCommands)

    @staticmethod
    def printGradeMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1. Add a grade \n'
        string += '\t 2. Display all grades \n'
        string += '\t 0. Back to main menu \n'
        print(string)

    @staticmethod
    def validGradeCommand(command):
        """
            checks if the given command is a valid one
            Input: command - the given command - string
            Output: True - if the command is a valid ID command
                    False - otherwise
            """
        availableCommands = ['1', '2', '0']
        return (command in availableCommands)

    @staticmethod
    def printStatisticsMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1. Display all students at a discipline sorted alphabetically \n'
        string += '\t 2. Display the failing students \n'
        string += '\t 3. Display the top students \n'
        string += '\t 4. Display the disciplines sorted based on their average\n'
        string += '\t 0. Back to main menu \n'
        print(string)

    @staticmethod
    def validStatisticsCommand(command):
        """
            checks if the given command is a valid one
            Input: command - the given command - string
            Output: True - if the command is a valid ID command
                    False - otherwise
            """
        availableCommands = ['1', '2', '3', '4', '0']
        return (command in availableCommands)

    @staticmethod
    def readPositiveInteger(msg):
        """
        reads a positive integer
        Input: msg - what message will be displayed to the user
        Output: A positive integer
        """
        res = 0
        while True:
            try:
                res = int(input(msg))
                if res < 0:
                    raise ValueError()
                break
            except ValueError:
                print("The value introduced is not a positive integer. ")
        return res

    @staticmethod
    def readGrade(msg):
        """
        reads a float between 1 and 10
        Input: msg - the message to be shown to the user before reading
        Output: a float number between 1 and 10
        """
        res = 0
        while True:
            try:
                res = float(input(msg))
                if res < 1 or res > 10:
                    raise ValueError()
                break
            except ValueError:
                print("The value introduced is not a number between 1 and 10. ")
        return res

    def __addDisciplineMenu(self):
        """
        adds a Discipline to the list
        Input: none
        Output: a new Discipline is read and added (assuming there is no discipline with the same ID already)
        """
        ID = UI.readPositiveInteger("Please enter the discipline ID: ")
        name = input("Please enter the discipline name: ")

        try:
            dis = Discipline(ID, name)
            self.__disCtrl.addDiscipline(dis)
        except DisciplineException as ex:
            print(ex)

    def __updateDisciplineMenu(self):
        """
        updates a Discipline from the list
        Input: none
        Ouput: the Discipline is updated, if it is in the list
        """
        ID = UI.readPositiveInteger("Please enter the discipline ID: ")
        newname = input("Please enter the discipline's new name: ")

        try:
            self.__disCtrl.updateDiscipline(ID, newname)
        except DisciplineException as ex:
            print(ex)

    def __removeDisciplineMenu(self):
        """
        removes a Discipline from the list
        Input: none
        Output: the Discipline is removed, if it exists
        """
        ID = UI.readPositiveInteger("Please enter the discipline ID: ")

        try:
            self.__disCtrl.removeDiscipline(ID)
        except (DisciplineException, GradeException) as ex:
            print(ex)

    def __searchDisciplineByIDMenu(self):
        """
        searches disciplines based on a given ID
        Input: none
        Output: the Discipline with the given ID is displayed if it exists
        """
        ID = UI.readPositiveInteger("Please enter the discipline ID: ")
        res = self.__disCtrl.searchDisciplineID(ID)
        if res == None:
            print("No discipline matches the given ID.")
        else:
            print(res)

    def __searchDisciplineByStringMenu(self):
        """
        searches disciplines based on a given string
        Input: none
        Output: the Disciplines that match the string are displayed
        """
        string = input("Please enter the string: ")
        res = self.__disCtrl.searchStringinNameDiscipline(string)
        if res == []:
            print("No discipline matches the given string")
        else:
            print("The following disciplines match the string: ")
            for dis in res:
                print(dis)

    def __showAllDisciplinesMenu(self):
        """
        shows all the disciplines
        """
        dis = self.__disCtrl.getAll()
        if len(dis) == 0:
            print("There are no disciplines in the register.")
        else:
            for d in dis:
                print(d)

    def DisciplineMenu(self):
        commandDict = {'1': self.__addDisciplineMenu,
                       '2':self.__updateDisciplineMenu,
                       '3':self.__removeDisciplineMenu,
                       '4':self.__searchDisciplineByIDMenu,
                       '5':self.__searchDisciplineByStringMenu,
                       '6':self.__showAllDisciplinesMenu}

        while True:
            UI.printDisciplineMenu()
            command = input("Please enter your command: ")
            while not UI.validDisciplineCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()

    def __addStudentMenu(self):
        """
        adds a Student to the list
        Input: none
        Output: a new Student is read and added (assuming there is no student with the same ID already)
        """
        ID = UI.readPositiveInteger("Please enter the student ID: ")
        name = input("Please enter the student name: ")

        try:
            stu = Student(ID, name)
            self.__stuCtrl.addStudent(stu)
        except StudentException as ex:
            print(ex)

    def __updateStudentMenu(self):
        """
        updates a Student from the list
        Input: none
        Ouput: the Student is updated, if it is in the list
        """
        ID = UI.readPositiveInteger("Please enter the student ID: ")
        newname = input("Please enter the student's new name: ")

        try:
            self.__stuCtrl.updateStudent(ID, newname)
        except StudentException as ex:
            print(ex)

    def __removeStudentMenu(self):
        """
        removes a Student from the list
        Input: none
        Output: the Student is removed, if it exists
        """
        ID = UI.readPositiveInteger("Please enter the student ID: ")

        try:
            self.__stuCtrl.removeStudent(ID)
        except (StudentException, GradeException) as ex:
            print(ex)

    def __searchStudentByIDMenu(self):
        """
        searches students based on a given ID
        Input: none
        Output: the Discipline with the given ID is displayed if it exists
        """
        ID = UI.readPositiveInteger("Please enter the student ID: ")
        res = self.__stuCtrl.searchStudentID(ID)
        if res == None:
            print("No student matches the given ID.")
        else:
            print(res)

    def __searchStudentByStringMenu(self):
        """
        searches students based on a given string
        Input: none
        Output: the students that match the string are displayed
        """
        string = input("Please enter the string: ")
        res = self.__stuCtrl.searchStringinNameStudent(string)
        if res == []:
            print("No student matches the given string")
        else:
            print("The following students match the string: ")
            for stu in res:
                print(stu)

    def __showAllStudentsMenu(self):
        """
        shows all the students
        """
        stu = self.__stuCtrl.getAll()
        if len(stu) == 0:
            print("There are no students in the register.")
        else:
            for s in stu:
                print(s)

    def StudentMenu(self):
        commandDict = {'1': self.__addStudentMenu,
                       '2': self.__updateStudentMenu,
                       '3': self.__removeStudentMenu,
                       '4': self.__searchStudentByIDMenu,
                       '5': self.__searchStudentByStringMenu,
                       '6': self.__showAllStudentsMenu}

        while True:
            UI.printStudentMenu()
            command = input("Please enter your command: ")
            while not UI.validStudentCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()

    def __addGradeMenu(self):
        """
        adds a Grade to the list
        Input: none
        Output: a new Grade is read and added (assuming there that given ID's for student and discipline are valid)
        """
        disciplineID = UI.readPositiveInteger("Please enter the discipline ID: ")
        studentID = UI.readPositiveInteger("Please enter the student ID: ")
        grade = UI.readGrade("Please enter the grade")

        try:
            gra = Grade(disciplineID, studentID, grade)
            self.__graCtrl.addGrade(gra)
        except (GradeException, DisciplineException, StudentExcetpion) as ex:
            print(ex)

    def __showAllGradesMenu(self):
        """
        shows all the grades
        """
        gra = self.__graCtrl.getAll()
        if len(gra) == 0:
            print("There are no grades in the register.")
        else:
            for g in gra:
                print(g)

    def GradeMenu(self):
        commandDict = {'1': self.__addGradeMenu,
                       '2': self.__showAllGradesMenu}

        while True:
            UI.printGradeMenu()
            command = input("Please enter your command: ")
            while not UI.validGradeCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()

    def __byDisciplineAlphabetically(self):

        ID = UI.readPositiveInteger("Please enter the discipline ID: ")
        try:
            res = self.__staCtrl.byDisciplineAlphabetically(ID)
            if res == []:
                print("There are no students graded at the given discipline")
            else:
                for i in range(len(res)):
                    string = str(res[i][0]) + " NAME " + str(res[i][1])
                    print(string)
        except DisciplineException as e:
            print(e)

    def __failingStudents(self):

        res = self.__staCtrl.failingStudents()
        if res == []:
            print("There are no students")
        else:
            for i in range(len(res)):
                string = str(res[i][0]) + " NAME " + str(res[i][1])
                print(string)

    def __topStudents(self):

        res = self.__staCtrl.topStudents()
        if res == []:
            print("There are no students")
        else:
            for i in range(len(res)):
                string = str(res[i][1]) + " NAME " + str(res[i][2]) + " AVERAGE " + str(res[i][0])
                print(string)

    def __topDiscipline(self):

        res = self.__staCtrl.topDiscipline()
        if res == []:
            print("There are no disciplines")
        else:
            for i in range(len(res)):
                string = str(res[i][1]) + " NAME " + str(res[i][2]) + " AVERAGE " + str(res[i][0])
                print(string)

    def StatisticsMenu(self):
        commandDict = {'1': self.__byDisciplineAlphabetically,
                       '2': self.__failingStudents,
                       '3': self.__topStudents,
                       '4': self.__topDiscipline}

        while True:
            UI.printStatisticsMenu()
            command = input("Please enter your command: ")
            while not UI.validStatisticsCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()

    def UndoMenu(self):

        res = self.__undoCtrl.undo()
        if res == True:
            print("Undo successfully made.")
        else:
            print("Undo can not be performed")

    def RedoMenu(self):

        res = self.__undoCtrl.redo()
        if res == True:
            print("Redo successfully made.")
        else:
            print("Redo can not be performed")

    def MainMenu(self):

        commandDict = {'1': self.DisciplineMenu,
                       '2': self.StudentMenu,
                       '3': self.GradeMenu,
                       '4': self.StatisticsMenu,
                       '5': self.UndoMenu,
                       '6': self.RedoMenu}

        while True:
            UI.printMenu()
            command = input("Please enter your command: ")
            while not UI.ValidInputCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()