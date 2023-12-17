class Student:
    def method1(self):
        print("parent nethod1")

    def method2(self):
        print("parent nethod2")

    def method3(self):
        print("parent nethod3")


# ==========================================

class CSE(Student):
    def method3(self):
        print("child method 4")


# ================================================

s1 = CSE()
s1.method1()
s1.method3()
# =====================================
x = "This is saha Shoykat"
print(len(x))
for i in x:
    print(i)


for m in range(1, 5):
    print(m)
print("========================================================================")

p = list(range(1,10,2))
for m in  p:
    print(m)


#==============================================================
my_list = list()
my_list= list([1,2,3,4,5,6])
print(my_list)
my_list.append("saha")
print(my_list)
print(len(my_list))

my_list.remove(my_list[2])
print(my_list)
print(my_list[5:1:-1])
#my_list.remove()
