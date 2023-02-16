class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printinfo(self):
    print(f"Hello my name is {self.name} and my age is {self.age}")

person1 = Person("Erick", 23)
person1.printinfo()

person2 =Person("Collo", 18)
person2.printinfo()

class Employees:
  def __init__(self, fname, office):
    self.fname = fname
    self.office = office
  def printinfo(self):
   print(f"{self.fname} is our {self.office}")

person1 =Employees("Collins", "Manager")
person1.printinfo()
person2 =Employees("Kimberely", "Secretary")
person2.printinfo()

class MyCompany:
  def __init__(self,compname,revenue):
    self.name = compname
    self.revenue =revenue
  def productivity(self):
   print(f"{self.name} gets {self.revenue}")

person1 =MyCompany("Mitchelcots", 40000)
person1.productivity()
person2 =MyCompany("Safaris", 30000)
person2.productivity()
