def printing(x):
    print(x)

def printing1(x):
    print(x[2])

def print_loop(x):
    for y in x:
        print(y)

def check(x):
    if "apple" in x:
        print("Match found!")

def count(x):
    print(len(x))

def tuple_Add_Odd(y):
    result = 0
    for x in y:
        if x % 2 != 0:
            result+=x
    return result

def tuple_Add_Even(y):
    result = 0
    for x in y:
        if x % 2 == 0:
            result+=x
    return result

def tuple_Multiply_Odd(y):
    result = 1
    for x in y:
        if x % 2 != 0:
            result*=x
    return result

def tuple_Multiply_Even(y):
    result = 1
    for x in y:
        if x % 2 == 0:
            result*=x
    return result
def tuple_counter(tuple,num):
    return str(tuple.count(num))

printing(("apple", "banana", "orange"))
printing1(("apple", "banana", "orange"))
print_loop(("apple","banana", "orange"))
check(("apple","banana", "orange"))
count(("apple","banana", "orange"))
print(tuple_Add_Odd(((1,2,3,4,5,6,7))))
print(tuple_Add_Even(((1,2,3,4,5,6,7))))
print(tuple_Multiply_Odd(((1,2,3,4,5,6,7))))
print(tuple_Multiply_Even(((1,2,3,4,5,6,7))))
print(tuple_counter(((1,1,1,2,3,4,4,1)),1))
