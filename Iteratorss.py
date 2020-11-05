from itertools import permutations,accumulate,groupby,product

def less_than_3(x):
    return x<5


l1=[2,3,4,8,9]
prod=permutations(l1)

print(list(prod))

acc=accumulate(l1)
print(list(acc))

grp=groupby(l1,key=less_than_3)

for key,values in grp:
    print(key,list(values))

a=range(1,100,2)

print(list(a))



