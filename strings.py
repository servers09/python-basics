def split(x):
	return str(x.split(" "))

def concatenate(a):
	x = "com"
	y = (str(x) + str(a))
	return y

def length(a):
	b = len(a)
	return b

def position(a):
	return str(a[5])

def whitespace(a):
	return a.strip()

def lowercase(a):
	return str(a.lower())

def uppercase(a):
	return str(a.upper())

def forloop(a):
	for i in a:
		print(a)

def whileloop(a):
	b= len(a) - 1
	while b >= 0:
		print(a[b])
		b-=1

def ifstate(n):
	n = len(n)
	x = len("two")
	if x == n:
		return str("Match")
	else:
		return str("Unmatch")

def elifstate(n):
	n = len(n)
	x = len("lover")
	if x == n:
		return str("Match")
	elif n<x:
		return str("Add more")
	else:
		return str("Mismatch")

def range(n):
	return str(n[3:6])

def names():
	n = ["Vince", "Eric", "John", "Jalina"]
	for x in n:
		print(x)

def numbering():
	n = ["wow", "meow", "moo"]
	for a, b in enumerate(n):
		print(a, b)

def replace(n):
	x = (n.replace("n", "d"))
	return x

def check():
	n = ["hi", 5, "me", 4 , 24, 65]
	if  "hi" in n:
		return str("Match Found")
	else:
		return str("Does not exist")

def counter():
	n = ["wow", 6, 'hello', 6, 6, 1]
	x = (n.count(1))
	return x

def int_convert_to_str(n):
	return str(n)

def adding():
	a = "Hello"
	b = "Hi"
	c = a + b
	return str(len(c))

def subtracting():
	a = "words"
	b = "moneymaking"
	x = len(a)
	y = len(b)
	c = x - y
	return str(c)






print(split("a b c d e f"))
print(concatenate("bine"))
print(length("abcdefghijklmnopqrstuvwxyz"))
print(position("sample"))
print(whitespace("Hello World"))
print(lowercase("SAMPLE TEXT"))
print(uppercase("hey there"))
forloop("Vince")
whileloop("reverse")
print(ifstate("one"))
print(elifstate("bottle"))
print(range("sniper"))
names()
numbering()
print(replace("nick"))
print(check())
print(counter())
print(int_convert_to_str(24243465))
print(adding())
print(subtracting())
