"""#using inheritance employee id(parent and child class)
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

#test modified to inheritance(parent class and child class)g
class Inventory:
    def _init_(self):
        self.prodid=int(input('enter Id'))
        self.prodname=input('enter name')
        self.prodcount=int(input('enter the count'))
    
class Display(Inventory):
    def show(self):
        print('Product name',self.prodid,'product name',self.prodname,'product count',self.prodcount)
    
d=Display()
d.show()"""


#multiple inheritance(many parent one child )
class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId:{self.Id}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressInfo(self):
        print(f"Street Name: {self.street}\nState Name:{self.state}\nCountry name: {self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)#ipdiyum panalam
        Address.__init__(self,street,state,country)#or ipdiyum pannalam any one only
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayaddressInfo()
ed=EmployeeDetails("Jiya",100,"Manager","Shenoy Nagar","TamilNadu","India")
ed.displayEmp()
        
