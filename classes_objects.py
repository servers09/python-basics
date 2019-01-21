class MyClass:
  x = 5 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class compare:
    def less_than(self,num1,num2):
        if num1 < num2:
            return True
        else:
            return False
    print(less_than("blank",3,5))
 

    def greater_than(self,num1,num2):
        if num1 > num2:
            return True
        else:
            return False
    print(greater_than("blank",3,5))

    def equal(self,num1,num2):
        if num1 == num2:
            return True
        else:
            return False
    print(equal("blank",3,5))

class odd_even_verify:
    def __init__(self,num):
        self.num = num
    def bool_odd(self):
        if self.num % 2 != 0:
            return True
        else:
            return False
    def bool_even(self):
        if self.num % 2 == 0:
            return True
        else:
            return False
        

p = MyClass()
print(p.x)
p = Person("John", 36)
print(p.name)
print(p.age)
odd_even = odd_even_verify(4)
print(odd_even.bool_odd())
print(odd_even.bool_even())
