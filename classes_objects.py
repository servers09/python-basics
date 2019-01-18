class MyClass:
  x = 5
p = MyClass()
print(p.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p = Person("John", 36)
print(p.name)
print(p.age)

class compare:
    def less_than(self,num1,num2):
        if num1 < num2:
            return True
        else:
            return False

    def greater_than(self,num1,num2):
        if num1 > num2:
            return True
        else:
            return False
        
    def equal(self,num1,num2):
        if num1 == num2:
            return True
        else:
            return False
