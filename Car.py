import threading

class Car():

    def __init__(self,name,model):
        self.name=name
        self.model=model


    def driver(self,d_name):
        print("The car is Droven by",d_name)


    def speed(self,km):
        print("The speed of car is :",km)

    def display(self):
        print("Name "+self.name+" Model: "+self.model)

from threading import Thread

class BMW(Car,Thread):

    def __init__(self,name,model,price):
        Thread.__init__(self)
        super(BMW, self).__init__(name,model)

        self.price=price

    def display(self):
        super().display()
        print("The Price of a car is: ",self.price)


    def run(self):
        global sum
        if threading.current_thread().getName()=="bm":
            for i in range(0,5):
                #print(sum)
                sum += i
        else:
            for i in range(5,11):
                #print(sum)
                sum += i



sum=0
BM=BMW("BMW","XUV",20000)
BM.display()
BM.speed(20000)
BM.driver("Dhiraj Gidde")

BM1=BMW("dasd","cas",45545)

BM.setName("bm")

BM.start()

BM1.start()
print(sum)
