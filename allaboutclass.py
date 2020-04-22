class Student:
    def __init__(self,name,age,school,grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
    
    def subjectTaking(self,subject):
        print(f'{self.name} is taking {subject}')


student1 = Student('Kartik Alle', 16, 'Enloe HS', 10)
print(student1.__dict__)
student1.subjectTaking('Calculus')