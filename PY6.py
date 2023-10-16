# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:15:45 2023

@author: samue
"""

import numpy as np
import math


'''x=np.zeros(5)
print(x)

nel=int(input('Enter number elements in the vector : '))
lvec=[]#create empty list
for i in range (nel):
    comp=input(f'Enter the value of component {i} : ')
    lvec.append(float(comp))#convert it to real and add it to lvec
vec=np.array(lvec)#create array form list
print(vec)

nel=int(input('Enter number elements in the vector : '))
vec=np.zeros(nel)
for i in range (nel):
    comp=input(f'Enter the value of component {i} : ')
    vec[i]=float(comp)#we convert it to real and assign it to the 'i  component of vec
print(vec)

lin=input('Enter components of a vector in a line : ')
smooth=lin.split()#separate the line considering the targets
vec=np.float_(smooth)#look the back of the np float /!\ a l'underscore
print(f'List : {smooth}')
print(f'Vector : {vec}')

mat=np.zeros((4,3))
for i in range(4):
    for j in range (3):
        mat[i,j]=float(input(f'Value of element ({i},{j}) : '))
print(mat)

A=[[2,3],[1,2]]
B=[[1,0],[3,1]]
AB=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        mem=0
        for k in range(2):
            mem+=A[i][k]*B[k][j]
        AB[i][j]=mem
print(AB)

invAB=np.linalg.inv(AB)
print(invAB)

invA=np.linalg.inv(A)
invB=np.linalg.inv(B)
invBinvA=invB@invA
print(invBinvA)

print()

A=[[1,1],[1,2]]
B=[[4,1],[3,1]]
C=[[24,7],[31,9]]
X=np.linalg.inv(A)@C@np.linalg.inv(B)
print(X)

print()

H=[2.07*10**-5,2.62*10**-7,3.22*10**-5,2.59*10**-4,4.87*10**-5,1.019*10**-4,3.95*10**-5]
pH=[0,0,0,0,0,0,0]
for i in range(7):
    pH[i]=-1*math.log10(H[i])
print(pH)'''

#exercice 1
print('exercice 1')
angtroms = np.linspace(1.0,5.0,21)
nm = 0.1*angtroms
print(nm)

print()

#exercice 2
print('exercice 2')
x0=float(input('x0 : '))
s=float(input('s : '))
min=int(input('initial value of x : '))
max=int(input('final value of x : '))
n=int(input('n : '))
mat=np.zeros((2,n))
for i in range(n):
    mat[0][i]=min+i*(max-min)/(n-1)
    mat[1][i]=(math.exp(-((mat[0][i]-x0)**2)/2*s**2))/math.sqrt(2*math.pi)
print(mat)

print()

#exercice 3
print('exercice 3')
temp_mat = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
mat = np.array(temp_mat)
avg=0
for element in mat:
    avg+=element
print(f'Average temperature : {avg/12}')
min=0
max=0
for i in range(mat.size):
    if mat[i]<mat[min]:
        min=i
    if mat[i]>mat[max]:
        max=i
print(f'Max temperature : {months[max]}, {mat[max]}')
print(f'Min temperature : {months[min]}, {mat[min]}')

print()

#exercice 4
print('exercice 4')
n=int(input('number of students : '))
mat=np.zeros((n,4))
max=0 
min=0
avg=0
for i in range(n):
    mat[i][0]=i
    mat[i][1]=float(input(f'Student {mat[i][0]} theory part : '))
    mat[i][2]=float(input(f'Student {mat[i][0]} exam part : '))
    mat[i][3]=mat[i][1]*0.4+mat[i][2]*0.6
    if mat[i][3]>mat[max][3]:
        max=i
    if mat[i][3]<mat[min][3]:
        min=i
    avg+=mat[i][3]
avg=avg/n
print(f'Min student {min} : {mat[min][3]}/10')
print(f'Max student {max} : {mat[max][3]}/10')
print(f'Average : {avg}/10')


