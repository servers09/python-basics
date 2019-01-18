def bool_while(n):
    while True:
        if n == 4:
            return True
            break
        else:
            return False

def bool_for(b):
    a=0
    for i in b:
        return bool(i)
    a+=1

def int_while(a):
    while a<6:
        print(a)
        a+=1

def int_while_break(a):
    while a<10:
        print(a)
        if (a==3):
            break
        a+=1
def list_fruit(food):
    for x in food:
        print (x)
def string_for(food):
    for x in food:
        print(x)
def string_for_break(food):
    for x in food:
        print(x)
        if x== "cherry":
            break
def string_for_break2(food):
    for x in food:
        if x== "rice":
            break
        print(x)
def int_for(y):
    for x in range(y):
        print(x)
def string_for_list(adj,food):
    for x in adj:
        for y in food:
            print(x,y)
            
print(bool_while(0))
print(bool_for([1]))
int_while(0)
int_while_break(1)
list_fruit(["chicken","rice", "cherry", "coffee"])
string_for("orange")
string_for_break(["chicken","rice", "cherry", "coffee"])
string_for_break2(["chicken","rice", "cherry", "coffee"])
int_for(5)
string_for_list(["red", "big", "tasty"],["apple", "banana", "cherry"])
