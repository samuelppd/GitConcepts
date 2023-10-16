# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:11:52 2023

@author: samue
"""

import numpy as np

#Write a NumPy program to create a vector 
#with values from 0 to 20 and change the 
#sign of the numbers in the range from 9 
#to 15.
vec=np.arange(21)
vec[9:16]=-vec[9:16]
'''for i in range(len(vec)):
    if vec[i]>=9 and vec[i]<=15:
        vec[i]=-vec[i]'''
print(vec)
print()

#Write a NumPy program to create a vector 
#with values ranging from 15 to 55 and 
#print all values except the first and last.
vec=np.arange(15,56)  
print(vec[1:-1])
print()

#WWrite a NumPy program to create a 3X4 
#array and iterate over it.
mat=np.zeros((3,4))
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        mat[i][j]=i*mat.shape[1]+j
print(mat)
print()

#Write a NumPy program to create a vector 
#of length 10 with values evenly distributed 
#between 5 and 50.
vec=np.linspace(5,50,10)
print(vec)
print()

#Write a NumPy program to create a vector 
#of length 5 filled with arbitrary integers 
#from 0 to 10.
vec=np.random.randint(0,10,5)
print(vec)
print()

#Write a NumPy program to multiply the values 
#of two given vectors.
vec1=np.linspace(0,2,3)
vec2=np.linspace(3,5,3)
vec=vec1*vec2
print(f'{vec1}*\n{vec2}=\n{vec}')
print()

#Write a NumPy program to create a 3x4 matrix 
#filled with values from 10 to 21.
mat=np.random.randint(10,21,size=(3,4))
print(mat)
print()

#Write a NumPy program to find the number of 
#rows and columns in a given matrix.
mat=np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]])
print(f'Matrix has {mat.shape[0]} rows and {mat.shape[1]} columns.')

#Write a NumPy program to create a 4x4 matrix 
#in which 0 and 1 are staggered, with zeros 
#on the main diagonal.
mat=np.ones((4,4))
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        if (i+j)%2==0:
            mat[i][j]=0
print(mat)
print()

#Write a NumPy program to find common values 
#between two arrays. Expected Output:
#Array1: [ 0 10 20 40 60]
#Array2: [10, 30, 40]
#Common values between two arrays:
#[10 40]
vec1=np.array([0,10,20,40,60])
vec2=np.array([10,30,40])
vec=np.intersect1d(vec1,vec2)
print(vec)
print()

#Write a NumPy program to get the unique elements 
#of an array. Expected Output:
#Original array: [10 10 20 20 30 30]
#Unique elements of the above array: [10 20 30]
#Original array: [[1 1],[2 3]]
#Unique elements of the above array: [1 2 3]
vec1=np.array([10,10,20,20,30,30])
vec=np.unique(vec1)
print(vec)
vec2=np.array([[1,1],[2,3]])
vec=np.unique(vec2)
print(vec)
print()

#Write a NumPy program to compute the cross 
#product of two given vectors.
vec1=np.array([1,2,3])
vec2=np.array([4,5,6])
vec=np.cross(vec1,vec2)
print(vec)
print()

#Write a NumPy program to convert cartesian 
#coordinates to polar coordinates of a random 
#10x2 matrix representing cartesian coordinates.
#Expected Output:
#[ 0.89225122 0.68774813 0.20392039 1.22093243 
# 1.24435921 1.00358852 0.37378547 0.8534585 
# 0.31999648 0.567451 ],[ 1.02751197 1.26964967 
# 0.02567519 0.85386412 0.73152767 0.45822494
# 1.50634505 1.47389983 0.80818521 0.33001182]
mat=np.random.uniform(0,1,size=(2,10))
x = mat[:, 0]
y = mat[:, 1]
radius = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
theta_degrees = np.degrees(theta)
polar_coordinates = np.column_stack((radius, theta_degrees))
print("Cartesian Coordinates:")
print(mat)
print("\nPolar Coordinates:")
print(polar_coordinates)
print(mat)
print()

#Write a NumPy program to find the closest value 
#(to a given scalar) in an array.
#Original array: [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61
# 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77
# 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93
# 94 95 96 97 98 99]
#Value to compare: 34.99062268928913 35
mat=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
              16,17,18,19,20,21,22,23,24,25,26,27,28,
              29,30,31,32,33,34,35,36,37,38,39,40,41,
              42,43,44,45,46,47,48,49,50,51,52,53,54,
              55,56,57,58,59,60,61,62,63,64,65,66,67,
              68,69,70,71,72,73,74,75,76,77,78,79,80,
              81,82,83,84,85,86,87,88,89,90,91,92,93,
              94,95,96,97,98,99])
sca=34.99062268928913
val=mat[np.argmin(np.abs(mat - sca))]
print(val)
sca=35
val=mat[np.argmin(np.abs(mat - sca))]
print(val)


