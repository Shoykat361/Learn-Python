class Student:
    def method1(self):
        print("parent nethod1")
    def method2(self):
        print("parent nethod2")
    def method3(self):
        print("parent nethod3")

#==========================================

class CSE (Student):
    def method3(self):
        print("child method 4")

#================================================

s1 = CSE()
s1.method1()
s1.method3()
