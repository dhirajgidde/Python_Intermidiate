import array as arr


def smallestNuber(arrr):
    small = 99
    second_smallest=0
    for i in range(0,len(arrr)):
        if(arrr[i]<small):
            second_smallest=small
            small=arrr[i]
        if(second_smallest>arrr[i] and arrr[i]>small):
            second_smallest=arrr[i]

    print("The Second smallest Value is :",second_smallest)


values=arr.array('i',[5,4,3,1,8,0,-2,-1,9,-3])
print(values)
smallestNuber(values)