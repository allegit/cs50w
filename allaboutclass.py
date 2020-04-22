'''
    This python code explains all about a python class
'''

class Student:
    def __init__(self,name,age,school,grade):
        print('__init__ method gets called')
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
    
    def __new__(cls,*args):
        print('__new__ method gets called...')
        student = object.__new__(cls)
        return student

    def subjectTaking(self,subject):
        print(f'{self.name} is taking {subject}')

student1 = Student('Kartik Alle', 16, 'Enloe HS', 10)
print(student1.__dict__)
print(type(student1))
student1.subjectTaking('Calculus')

# Usage of the '__new__' method, creating a new instance of the class
# whereas the '__init__' method initializes the new instance of the class.

student2 = object.__new__(Student)
student2.__dict__
Student.__init__(student2, 'Ritvik Alle', 13, 'Carnage MS', 7)
print(type(student2))
print(student2.__dict__)
