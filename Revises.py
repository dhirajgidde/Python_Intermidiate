import sys

a = "hello"
b = 2.5
c = 33

print(a, b, c)

#These is a single line comment
'''
    These is a multi line
    comment
'''

#String are immutable in python

str="Wellcome"
str1=str.join('Tata')
print(str[::-1])
print(str[0:2])
print(str1)
print(str.count("l"))#Character Count in string
print(str.replace("ll","WW"))
print(str)
print(str.title())
print(str.upper())
print(str)

#List
lst=[1,"We",2.5,"Are","Proud"]
print(lst)
print(lst[::-1])
lst.append("NANA")
print(lst)
lst.insert(1,220)
print(lst)
print(lst[1:4])

#Tuple Tuples are immutable in python

tup=(1,2,3,4,4,5)
print(tup.count(4))
print(tup)

#Dict
dct={'a':1,
     'b':1234.5,
     3:"WElcome"}

print(dct[3])
print(dct.items())
print(dct.values())
print(dct.get('a'))
#print(dct.clear())
print(dct.keys())
#print(dct.pop('a'))
print(dct)
dct['a']="Teo"
dct[5]="LY"
print(dct)

#Sets Sets cannot allow the duplicate element and always follow sorted order
print(set(tup))

#WE Can perform union,intersection and disjoint operation on set


st={11,2,3,4,5}
st.add(60)
st.add(5)
print(st)

import array as arr

ass=arr.array('i',[1,2,3,5])
print(ass.insert(1,5))

print(ass)
llt=list(ass)
print(type(llt))

for i in range(5,10):
    print(i)

l=0

while l<10:
    print(l)
    l+=1


def func():
    return 1,2,3,4

print(type(func()))

lst=[1,2,3,4,5]
lst1=[5,6,7,8,9]

lst3=[]
for i in range(len(lst)):
    lst3.append(lst[i]+lst1[i])

print(lst3)


for i in [1,2,3,4,5]:
    pass
    if(i==4):
        pass
        print("This is pass block",i)
    print(i)