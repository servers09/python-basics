def myfunction():
    print("Hello")

def text(fname):
    print(fname + " Refamonte")

def mul(x):
    return 5 * x

def div(x):
    return 5 / x

def int_Floor(x,y):
    result = x//y
    return result

def int_Exponent(x,y):
    result = x**y
    return result

def int_Modulo(x,y):
    result = x%y
    return result

def int_MDAS(x,y,z):
    result = x+y*z
    return result

def int_PEMDAS(x,y,z):
    result = (x+y)*z
    return result

def float_convert(kilo):
    result = float(kilo)*float(2.20462)
    return result

myfunction()
text("Vince")
print(mul(3))
print(div(3))
print(int_Floor(7,8))
print(int_Exponent(7,8))
print(int_Modulo(7,8))
print(int_MDAS(7,8,9))
print(int_PEMDAS(7,8,9))
print(float_convert(3))
