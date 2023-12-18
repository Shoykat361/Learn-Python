x = [1, 2, 3, 4, 5, 6, 7, 8]
'''a = list(x.reverse())
print(a)'''
a = list(reversed(x))  # Creates a reversed copy of x
print(a)
print(x)
x.pop(0)
print(x)
x.append("alex")
print(x)
'''x.__add__(1,"Saha")
print(x)'''

del x[len(x) - 1]
print(x)
x.pop()
print(x)

list1 = x.copy()
print(list1)
print(list1 + x)
list1.extend(x)
print(list1)
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 0, 3, 2, 4, 5, 5, 4, 4, 3, 4, 56, 6, 4, 3, 3, 2, 2, 1, 2, 3, 5, 6, 7, 8, 8, 3]
print(list2.count(3))
list2 = [1,2,3,4,5,5,6,7,8,8,9,10]
print(list2.count(1))
list2.insert(2,2.5)
print(list2)

def saha(x,y):
    print("sahatyttt")
    return x+y
w = saha(1,7)
print(w)
