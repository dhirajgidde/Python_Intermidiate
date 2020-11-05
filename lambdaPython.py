

add=lambda a,b: a+b
sub=lambda a,b: a-b
mul=lambda a,b: a*b
div=lambda a,b: a/b


print(add(12,13))
print(sub(12,13))
print(mul(12,13))
print(div(12,13))

try:
    x=10
    print(x)
except:
    print("An Errro is occured")
else:
    print("Nothing went WRong")
finally:
    print("WE are in finally")


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
