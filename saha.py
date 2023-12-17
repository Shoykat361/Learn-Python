'''
numberofletter = 0
numberofdigit = 0
numberofWord = 0
x = input("enter Some Things : ")
print(x)

for i in x:
    i.lower()
    if i >= 'a' and i <= 'z':
        numberofletter =numberofletter+1
    elif i>='0' and i<= '9':
        numberofdigit = numberofdigit+1
    elif i == ' ':
        numberofWord=numberofWord+1

print(numberofWord+1)
print(numberofdigit)
print(numberofletter)
'''

'''matrix = [
    [1,2,3,4,5],
    [4,5,6,7,8]
]
for row in matrix:
    for col in row:
        print(col)'''

'''saha ={
    "1": "Shoykat Saha",
    "2": "alex"
}
print(saha["1"])
'''

'''
def add(x, y):
    sum = x + y
    print(sum)


def minus(x, y):
    biog = x - y
    return biog


add(10, 22.4)
add(11, 23)
p = minus(5, 4)
print(p)

qq=(lambda a, b: a * a + 2 * a * b + b * b)(2, 3)
print(qq)
'''