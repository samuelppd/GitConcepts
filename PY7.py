# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:00:25 2023

@author: samue
"""

import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline

'''x=np.linspace(-2,2,101)
y=x**2
print(x)
plt.plot(x,y)
plt.title('Graph of x^2 vs x')
plt.show()
plt.plot(x) #y : number of points
plt.show()
plt.plot(y) #x : number of points
plt.show()'''

'''x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')
plt.show()'''

'''x=np.linspace(-2,2,101)
plt.xlabel('x')
plt.ylabel('f(x)')
y=x**2
plt.plot(x,y,'g',label='x^2') #g pour g(green)
y2=x**4
plt.plot(x,y2,'bo',label='x^4') #bo pour b(blue) o(dot)
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.title('Chart Title')
plt.legend()
# plt.savefig('fig1.png') # faire justa avant de show, sinon image blanche
plt.show()'''

'''nb=int(input('Number of points to draw : '))
x=np.linspace(-1,1,nb)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.cos(2*np.pi*x)
plt.plot(x,y,'bo',label='cos(2πx)')
y2=np.sin(2*np.pi*x)
plt.plot(x,y2,'violet',label='sin(2πx)')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.title('Trigonometry : cos(2πx) and sin(2πx)')
plt.legend()
plt.savefig('Trigonometry.png')
plt.show()'''

'''number=''
nb=0
while nb<=0:
    number=input('Number of points to draw : ')
    try:
        nb = int(number)
    except ValueError:
        print(ValueError)   
x=np.linspace(0,4,nb)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.sin(x*np.pi)*np.sin(20*x*np.pi)*np.exp(-x)
plt.plot(x,y,'b',label='sin(πx)sin(20πx)e^(-x)')
plt.xlim(0,4)
plt.title('sin(πx)sin(20πx)e^(-x)')
plt.legend()
plt.show()'''

'''R=0.08206
T=300

test = False
while test == False:
    nb = input("enter the number of points you want : ")
    try:
        int(nb)
    except:
        print("Enter a valid integer!")
    else:
        test = True
        nb = int(nb)

for i in range (5):
    test = False
    while test == False:
        T = input("enter temperature you want : ")
        try:
            int(T)
        except:
            print("Enter a valid integer!")
        else:
            test = True
            T = int(T)
    x=np.linspace(2,10,nb)
    y=(R*T)/x
    plt.plot(x,y,label='T='+str(T)+'K')

plt.xlabel('Vm')
plt.ylabel('p')
plt.xlim(2,10)
plt.title('p=(R*T)/Vm')
plt.legend()
plt.show()'''

#ex1
'''nb=int(input("Number of points to draw : "))
i=int(input("Initial value : "))
f=int(input("Final value : "))
x0=int(input("x0 : "))
s=float(input("s : "))

x=np.linspace(i,f,nb)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.exp(-(x-x0)**2/(2*s**2))/np.sqrt(2*np.pi)
plt.plot(x,y,'b')
plt.xlim(i,f)
plt.title('Gaussian Function')
plt.show()'''

#ex2
'''nb=int(input('Number of points to draw : '))
x=np.linspace(0,3,nb)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.exp(-x)
plt.plot(x,y,'b',label='e(-x)')
y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y2,'orange',label='sin(3πx)e(-x)')
plt.xlim(0,3)
plt.title('Functions')
plt.legend()
plt.show()'''

#ex3
'''nb = int(input("enter the number of points you want : "))
nbfct = int(input("enter the number of functions you want : "))
initial = int(input("enter the initial value you want : "))
final = int(input("enter the final value you want : "))'''