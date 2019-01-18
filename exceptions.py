def exept():
    try:
        print(x)
    except:
        print("An exception occurred")
def name():
    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")
def noError():
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
def final():
    try:
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
def write_error():
    try:
        f = open("demofile.txt")
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
def write():
    try:
        fh = open("testfile", "w")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print("Error: can\'t find file or read data")
    else:
        print("Written content in the file successfully")
        fh.close()
def temp_convert(var):
    try:
        return int(var)
    except :
        print ("The argument does not contain numbers")
def printing():
    try:
        print("hello")
    except:
        print("An exception occurred")
def add():
    try:
        print(x+y)
    except:
        print("An error occurred")
def add2():
    try:
        print(2+4)
    except:
        print("An error occurred")
exept()
name()
noError()
final()
write_error()
write()
temp_convert("xyz")
printing()
add()
add2()
