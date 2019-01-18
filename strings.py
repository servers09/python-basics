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
