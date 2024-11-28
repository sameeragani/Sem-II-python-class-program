#using inheritance employee id
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.sal=int(input("Enter the Salary:"))
    def displayInfo(self):
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()

#class and objects (test in class)
class Inventory:
    def _init_(self,proId,proName,prodCount):
        self.proId=proId
        self.proName=proName
        self.prodCount=prodCount
    def Display(self):
        print(f"proId{self.proId}\nproName{self.proName}\nprodCount{self.prodCount}")
a=Inventory(12335 ,"arins", 10)
a.Display()

#test modified to inheritance
class Inventory:
    def _init_(self):
        self.prodid=int(input('enter Id'))
        self.prodname=input('enter name')
        self.prodcount=int(input('enter the count'))
    
class Display(Inventory):
    def show(self):
        print('Product name',self.prodid,'product name',self.prodname,'product count',self.prodcount)
    
d=Display()
d.show()
