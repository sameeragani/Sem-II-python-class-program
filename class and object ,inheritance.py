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
d.show()


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
ed.displayEmp()"""


#mutlilevel inheritance(one parent many child(it will change according to the input we give))
"""class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name =", self.name, "\nAge =", self.age)
class Employee(Person):
    def __init__(self, name, age, Id):  
        super().__init__(name, age)  
        self.Id = Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id =", self.Id)
class Manager(Employee):
    def __init__(self, name, age, Id, Salary):
        super().__init__(name, age, Id) 
        self.Salary = Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary =", self.Salary)
man = Manager("Sam", 18, 2613, 10000)
man.displayManager()

#hierarchical inheritance(only one parent class many child)
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name =", self.name, "\nAge =", self.age)
class Student(Person):
    def __init__(self, name, age, roll_number):  
        super().__init__(name, age)  
        self.roll_number = roll_number
    def displayStudent(self):
        self.displayPerson()  
        print("Roll Number =", self.roll_number)
class Teacher(Person):
    def __init__(self, name, age, subject):  
        super().__init__(name, age) 
        self.subject = subject
    def displayTeacher(self):
        self.displayPerson()  
        print("Subject =", self.subject)
student = Student("Alice", 20, "S12345")
teacher = Teacher("Mr. John", 45, "Mathematics")
print("Student Details:")
student.displayStudent()
print("\nTeacher Details:")
teacher.displayTeacher()"""

"""#hybrid class
class Food:
    def __init__(self, name):
        self.name = name
    def display_food(self):
        print(f"Name: {self.name}")
class Nutrition(Food):
    def __init__(self, name, calories):
        super().__init__(name)
        self.calories = calories
    def display_nutrition(self):
        print(f"Calories: {self.calories}")
class Preparation(Nutrition):
    def __init__(self, name, calories, cooking_method):
        super().__init__(name, calories)
        self.cooking_method = cooking_method
    def display_preparation(self):
        print(f"Cooking Method: {self.cooking_method}")
class Origin(Preparation, Nutrition):
    def __init__(self, name, calories, cooking_method, origin):
        super().__init__(name, calories, cooking_method)
        self.origin = origin
    def display_origin(self):
        print(f"Origin: {self.origin}")
dish = Origin("Pizza", 250, "Baked", "Italy")
dish.display_origin()
dish.display_food()
dish.display_nutrition()
dish.display_preparation()"""

#hybrid class another example
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")
class Manager(Employee):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"ID: {self.ID}")
class Developer(Employee):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print(f"Department: {self.dept}")
class TeamLeader(Manager, Developer):
    def __init__(self, name, age, ID, dept, teamsize):
        Employee.__init__(self, name, age)
        self.ID = ID
        self.dept = dept
        self.teamsize = teamsize
    def displayTeamInfo(self):
        self.displayEmployeeInfo()
        print(f"ID: {self.ID}")
        print(f"Department: {self.dept}")
        print(f"Team size: {self.teamsize}")
Name = input("Enter the name: ")
Age = int(input("Enter the age: "))
ID = int(input("Enter the ID: "))
Dept = input("Enter the department: ")
Teamsize = input("Enter the team size: ")
tl = TeamLeader(Name, Age, ID, Dept, Teamsize)
tl.displayTeamInfo()
        
