class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    #초기화 메서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID

class Teacher(Person):
    #초기화 메서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, teacherID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.teacherID = teacherID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(subject:{0}, teacherID: {1})".format(self.subject, self.teacherID))
        print("Info(Name:{0}, Phone Number: {1}, subject:{2}, teacherID: {3})"
              .format(self.name, self.phoneNumber, self.subject, self.teacherID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "231122")
t = Teacher("바니프레소", "010-000-0000", "컴공", "180302")
p.printInfo()
s.printInfo()
t.printInfo()
print(p.__dict__)
print(s.__dict__)
print(t.__dict__)


