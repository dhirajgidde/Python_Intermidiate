
#to check the number is prime or not

def to_check_prime_or_not(num):
    list1=[]
    for j in range(3,num+1):
        for i in range(2,j):
            if(j%i==0):
                #print("The number is not prime.")
                break

        if(j%i!=0 and j%j==0):
           list1.append(j)

    print(list1)

number=int(input("Enter a number:"))
to_check_prime_or_not(number)