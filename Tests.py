import unittest
from Domain.Discipline import Discipline
from Domain.Discipline import testDis
from Domain.Grade import Grade
from Domain.Grade import testGra
from Domain.Student import Student
from Domain.Student import testStu
from Repository.DisciplineRepository import testDisRepo
from Repository.StudentRepository import testStuRepo
from Repository.GradeRepository import testGradeRepo
from Controller.DisciplineController import testDisController
from Controller.StudentController import testStuController
from Controller.GradeController import testGraController
from Controller.StatisticsController import testStaController
import sys
sys.path.append('/UBB/1st Year/FP/Assignment 5-7')

if __name__ == '__main__':
    unittest.main()
