# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

a=np.array([1,2,3],dtype='int32')
print(a)

print(a.ndim)#dimension = nbLignes
print(a.shape)#shape = nbColonnes x nbLignes
print(a.dtype)#type
print(a.size)#size = nbElement
print(a.itemsize)#itemsize = nbBytes / element
print(a.nbytes)#total size = nbBytes
print()

b=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)

print(b.ndim)
print(b.shape)
print(b.dtype)
print(b.size)
print(b.itemsize)
print(b.nbytes)
print()

c=np.array([[1,2,3,4,5,6],[3,4,5,6,7,8],[5,6,7,8,9,0]])
print(c)

print(c[1,5])#element
print(c[0,:])#ligne
print(c[:,2])#colonne
print(c[0,1::2])#1/2 element
print(c[0,1:-1:2])#1/2 element
print()

d=np.zeros((2,3))
print(d)
e=np.ones((2,3))
print(e)
f=np.random.rand(4,2)
print(f)
g=np.random.randint(-4,8,size=(3,3))
print(g)
h=np.identity(5)
print(h)
i=np.array([[1,2,3]])
print(i)
j=np.repeat(i,3,axis=0)
print(j)
k=np.ones((5,5))
k[1:-1,1:-1]=np.zeros((3,3))
k[2,2]=9
print(k)
print()

m=[[1,2,3],[4,5,6],[7,8,9]]
n=[[1,0,0],[0,2,0],[0,0,3]]
print(m)
print(n)
print(m*2)
print(m+n)
print(np.matmul(m,n))
print(np.matmul(n,m))
print(np.linalg.det(m))
print(np.linalg.det(n))
print(np.min(m,axis=0))
print(np.min(m,axis=1))

nbPoints=21
o=np.linspace(-2.0,2.0,nbPoints)
print(o)
p=np.arange(3,9,5)
print(p)


