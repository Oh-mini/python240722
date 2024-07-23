strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(str)  #print(strName)이면 전역변수 출력 / print(self.strName)이면 set된 msg 출력

d = DemoString()
d.set("First Message")
d.print()
