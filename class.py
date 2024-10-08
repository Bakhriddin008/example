class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) 
        self.graduationyear = 2019
        
    def printname(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 
x = Student("Mike", "Olsen")
x.printname()
