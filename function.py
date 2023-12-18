class Student():
    def sum(x,y,z):
        print("called")
        return y+z


student = Student()
ab =student.sum(1,4)
print(ab)

rerange = list(range(10))
print(rerange)

n = input("enter number")
list = n.split("-")
for i in list:
    print(i)

x = {1,2,3,3,4,5,6,7,6,5,6,4,3,2,3,4,5,3,2,1,1,1,}
print(x)
print(type(x))