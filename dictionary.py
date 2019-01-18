def display(x):
    print(x)

def change(x):
    x["year"]='1990'
    print(x)

def loop_print(x):
    for y in x:
        print(x[y])

def add_values(diction):
    result = 0
    for x in diction.values():
        result += x
    return result

def sub_values(diction):
    result = 0
    for x in diction.values():
        result -= x
    return result

def multiply_values(diction):
    result = 1
    for x in diction.values():
        result *= x
    return result

def length(x):
    print(len(x))

def dictionary_add(x):
    x["color"] = "blue"
    print(x)

def dictionary_remove(x):
    x.pop("model")
    print(x)

def dictionary_clear(x):
    x.clear()
    print(x)

display({"brand": "Toyota", "model": "Vios" , "year": "2018"})
change({"brand": "Toyota", "model": "Vios" , "year": "2018"})
loop_print({"brand": "Toyota", "model": "Vios" , "year": "2018"})
print(add_values(dict(a=4,b=2)))
print(sub_values(dict(a=4,b=2)))
print(multiply_values(dict(a=4,b=2)))
length({"brand": "Toyota", "model": "Vios" , "year": "2018"})
dictionary_add({"brand": "Toyota", "model": "Vios" , "year": "2018"})
dictionary_remove({"brand": "Toyota", "model": "Vios" , "year": "2018"})
dictionary_clear({"brand": "Toyota", "model": "Vios" , "year": "2018"})
