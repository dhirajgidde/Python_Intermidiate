
# file=open("geeks.text","a")
#
#
# file.write('''we are the engineers
# we knew how to deal with the world
# we are the future of the tomarrowssssss
# we can create, we can destroy
# don't mess with us, coz we are the engineers........''')
# file.write("The End-Game is here...")
# file.close()



with open("geeks.text","r") as file:
    data = file.read()
    word=data.split(" ")
    lines=data.split("\n")
    count = 0
    l_count=0

    for i in word:
        if i:
            count +=1

    for i in lines:
        if i:
            l_count+=1
    print("number of characters: ",len(data))
    print("Number of words: ",count)
    print("Number of lines in File: ",l_count)