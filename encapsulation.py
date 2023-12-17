class Student :
    def __init__(self,name,age,Id):
        self.__name = name
        self.__Id = Id
        self.age = age

    def See(self):
        print(f"Name= {self.__name},Age = {self.age} Id = {self.__Id}")
    def setName(self,name):
        self.__name = name
    def updateName(self):
        return self.__name



#=======================================================
student = Student("Shoykat ","22",182)
student.See()
'''student.age = 24
student.See()
student.__Id = 34
student.See()'''
student.setName("Alex")
print(student.updateName())
student.See()
print(student.__dir__())
student._
