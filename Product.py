

class Product():

    __id=0
    __name=""
    __price=0

    def __init__(self,id,name,price):
        self.__id=id
        self.__name=name
        self.__price=price

    def setId(self,id):
        self.__id=id

    def setName(self,name):
        self.__name=name

    def setPrice(self,price):
        self.__price=price

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def display(self):
        print("Id: ",self.getId()," Name: ",self.getName()," Price: ",self.getPrice())


p=Product(1,"Python",45454)
p.display()