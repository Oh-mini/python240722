class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    #f-string은 파이썬에서 문자열을 포맷팅하는 방법 중 하나로, 파이썬 3.6 버전부터 도입
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test():
    # Person 클래스 테스트
    p1 = Person(1, "John Doe")
    p1.printInfo()
    print()

    p2 = Person(2, "Jane Smith")
    p2.printInfo()
    print()

    # Manager 클래스 테스트
    m1 = Manager(3, "Alice Johnson", "Project Manager")
    m1.printInfo()
    print()

    m2 = Manager(4, "Bob Brown", "HR Manager")
    m2.printInfo()
    print()

    # Employee 클래스 테스트
    e1 = Employee(5, "Charlie Davis", "Python Developer")
    e1.printInfo()
    print()

    e2 = Employee(6, "Diana Evans", "Data Scientist")
    e2.printInfo()
    print()

    # 추가 테스트
    m3 = Manager(7, "Eva Green", "Marketing Manager")
    m3.printInfo()
    print()

    e3 = Employee(8, "Frank Harris", "Network Engineer")
    e3.printInfo()
    print()

    p3 = Person(9, "George Martin")
    p3.printInfo()
    print()

    p4 = Person(10, "Hannah Lee")
    p4.printInfo()
    print()

test()
