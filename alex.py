'''class Student :
    roll = " "
    name = " "
    def set_value(self,roll,name):
        self.roll=roll
        self.name = name
    def Display(self):
        print(f"Roll : {self.roll}, Name = {self.name}")


rahim = Student()
rahim.set_value(101,"Rahim Ahmed")
rahim.Display()
karim = Student()
karim.set_value(106,"Rahim hmed")
karim.Display()

_pale =121
print(pal-e)'''

# ========================================================================

'''class Student:
    def __init__(self):
        print("hello")
        print(self)


class Student1:
    def __init__(self):
        print("hello222")
        print(self)


# ===========================================================================================

x = Student()
x = Student1()
print(x)
print("x1", x)

print(x)
print("x1", x)
y = Student()
print("y", y)
'''

'''
class Student:
    def __init__(self):
        x = self
        print(x)
        print("hello")

    def Constractor(self, saha, alex=None, b=None):
        if saha != None and alex != None and b != None:
            print(saha * alex * b)
        elif alex != None and saha != None:
            print(saha * alex)
        else:
            print(1 * saha)

    def saha(self,*anyitem):
        sum = 0
        for x in  anyitem:
            sum = sum+x
        print(sum)


# =========================================================
x = Student()
x.Constractor(1)
x.Constractor(1, 2)
x.Constractor(1, 2, 3)
x.saha(5,2,1,2,3,6,7,9)
x.saha(5,2,1,2,3,6,7,9,1,2,1,1,1,1,1,1,1,1,1,)
'''


class Student:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __le__(self, other):
        return x,r


num1 = Student(10)
num2 = Student(5)
print(num1+num2)
print(num1 < num2)
