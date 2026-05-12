# really bad python code for SonarQube testing

import os
import math
from math import *
from random import *

password = "admin123"   # hardcoded secret
x = 0
y = 0
z = []

def calc(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
    try:
        if a == 1:
            return b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t
        elif a == 2:
            return b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t
        elif a == 3:
            return b/c
        elif a == 4:
            eval("print('unsafe eval')")   # security issue
        else:
            pass
    except:
        pass   # generic exception ignored


def duplicate1():
    a = 10
    b = 20
    c = 30
    if a < b:
        print("a smaller")
    else:
        print("b smaller")
    return a+b+c


def duplicate2():
    a = 10
    b = 20
    c = 30
    if a < b:
        print("a smaller")
    else:
        print("b smaller")
    return a+b+c


class test:
    def __init__(self,name,age,salary,address,phone,email):
        self.name=name
        self.age=age
        self.salary=salary
        self.address=address
        self.phone=phone
        self.email=email

    def show(self):
        print(self.name,self.age,self.salary,self.address,self.phone,self.email)


for i in range(0,100):
    if i % 2 == 0:
        print(i)
    else:
        print(i)

unused_variable = 999

while True:
    break

os.system("dir")   # command execution risk

print(calc(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
