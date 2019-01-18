def int_Add(x,y):
	result = x+y
	return result

def int_Sub(x,y):
	result = x-y
	return result

def int_Multiply(x,y):
	result = x*y
	return result

def int_Divide(x,y):
	result = x/y
	return result

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


print(int_Add(3,5))
print(int_Sub(3,5))
print(int_Multiply(3,5))
print(int_Divide(3,5))
print(int_Floor(3,5))
print(int_Exponent(3,5))
print(int_Modulo(3,5))
print(int_MDAS(3,4,5))
print(int_PEMDAS(3,4,5))
print(float_convert(2))
