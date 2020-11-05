
#We can pass any number of argument in args
def element(*args):
    for i in args:
        print(i)


element(["fdf","fdsf","fasfad","bye"],"ewre",455,5454)

#we can pass the key, value pair with any number of arguments

def element1(**kwargs):
    for key,value in kwargs.items():
        print("key: ",key," value: ",value)


element1(a="we",b="are",c=120,d=12.0)
