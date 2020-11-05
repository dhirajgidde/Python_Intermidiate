
#TOdays Agenda
'''
Array vs numpy
file handling
Thread
OOP
Regx
Arws & Kgws
1 Hour of Lecture..
Logical statement
'''

import numpy as np

# We can declare a N-Dimensional array through numpy called as ndarray


array=np.array([[1,2,3],[4,5,6]],dtype='complex') #complex array
 # array=np.array([[1,2,3],[4,5,6]]) Two diamenstional array
# array=np.array([1,2,3]) One diamestional array

print(array)

#to decide a datatype of a variable
dt=np.dtype([('age',np.int8)])
a=np.array([10,20,30],dtype=dt)
print(a['age'])

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
stud=np.array([('azbc',20,20.4),('axyz',21,21.5)],dtype=student)
print(np.sort(stud,order='name'))

print(stud['age'])


'''
'b' − boolean

'i' − (signed) integer

'u' − unsigned integer

'f' − floating-point

'c' − complex-floating point

'm' − timedelta

'M' − datetime

'O' − (Python) objects

'S', 'a' − (byte-)string

'U' − Unicode

'V' − raw data (void)
'''

#shape and Reshape

new_arr=np.array([[1,3,1],[2,5,9]])
print(new_arr.shape)
s=new_arr.reshape(3,2)
print(s)

#empty array

x=np.empty([3,2],dtype=int)
print(x)

import array as arr

a=arr.array("i",[1,2,3,4])
print(a)

a=np.arange(10)
print(a)

a=np.arange(10,50,2)
print(a)

#array slicing.
a=np.array([[1,2,3,4],[4,5,6,2],[2,5,11,34]])
print(a[1,...]) # take a second row
print(a[...,-1]) # take a last element of all coloumns
print(a[...,-1:]) # take a last element but resize it
print(a[...,1]) # second element from all the row


#Advanced Indexing

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

rows=np.array([[0,0],[2,2]])
cols=np.array([[0,2],[0,2]])

x=a[rows,cols]

print(x)


#lets check the transpose matrixs

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.T

print(b)

#trignometric function

a=np.array([0,90,180,270,360])

print(np.sin(a*np.pi/180))



