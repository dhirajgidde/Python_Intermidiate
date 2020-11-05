
# python uses 3 types of the data structures
'''
list
tuple
dict
set
array
'''


list1=['1','Welcome',2.0,'Happy']

list1.append("Heer")
list1.insert(3,"Character")


#list1.reverse()# reverse the element of list
#list1.remove(2.0) # remove the particular element
#list1.pop() # remove the last element
#list1.sort()
print(list1)

list2=[2,3,4]
list2.sort() # we can sort a list , but we have make them with specific datatype
print(list2)

list3=[2,4,5]



list4=[]

for i in range(0,len(list3)):
   list4.append(list2[i]*list3[i])

print(list4)


list5=[]
# for i in range(0,5):
#    value=int(input("Enter a value"))
#    list5.append(value)
#
# print(list5)


#tuple tuples are immutables in a python

t1=(1,2,3,4,5)
t2=list((2,4)) #type casting a tuple into list....

#print(t1+t2)

dicts={"1":"Dhiraj","2":"onkar",3:"Swapnil",4:"Shubham"}

dictss={2:2.0,3:5.0}

print(dicts.values())

print(dicts)