import sys
import math
#single line comment
"""
mutiline 
comment
"""
#Reading from a System Input
#input()
intake = []
#for line in sys.stdin:
    #intake.append(line)
x = 17
strng = 'Hello there'
str2 = "Hello there"
#no char in python!
b = True
bb = False
if x == 17:
    print("its true")
    if x > 12 and x < 19:
        pass

for x in range(10):
    print(x)
for x in range(1, 10):
    print(x)
lst = ["hi", 2, 7, 4, 6, 0, "bye"]
for v in lst:
    print(v)

x = 19
if x == 20:
    pass
elif x == 18:
    pass
elif x == 19:
    pass
else:
    pass
#no x++ or x--, only x+=1
x += 1
x = x+1
st = "hello there"
st[1]  # e
st[1:4]  # ell
st[:4]  # 0-4, hell
st[8:]  # 8-end, ere
st[-1]  # e
st[-2:]  # re

st[::2]  # everyother letter hlotee
st2 = "racecar"
st2 == st2[::-1]  # racecar, reversed

num1 = 1
num2 = 2
#num1+num2 doesnt work
int(num1)+int(num2)
str(1) == "1"
print("Hi"+str(2)+"Bob")

#math operators
numTest1 = int(1)
numTest2 = int(2)
#adding
print(numTest1+numTest2)
#subtracting
print(numTest2-numTest1)
#multiplying
print(numTest1*numTest2)
#dividing
print(numTest2/numTest1)
#squaring
print(numTest1**2)
#square rooting
print(math.sqrt(numTest1))
def some_function(param, param2):
    pass


class my_class():
    #when defining a method in a class, put self as first parameter. self = this in java
    def some_method(self, param, param2):
        pass

    def another_method(self):
        self.some_method(1, 2)
