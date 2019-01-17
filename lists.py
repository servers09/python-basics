def add():
	brands = ["MSI", "Asus", "Gigabyte"]
	brands.append("Zotac")
	brands.sort()
	return brands

def remove():
	brands = ["Zotac", "MSI", "Asus", "Gigabyte"]
	print("Before " + str(brands))
	brands.remove("Asus")
	return str("After " + str(brands))

def update():
	parts = {"HDD", "CPU", "GPU", "SSD"}
	parts.update(["Keyboard", "Mouse"])
	sorted(parts)
	return parts

def getvalue(num):
	return str(num.index(5))

def pop_values(letters):
	letters.pop()
	return letters

def reverse(x):
	x.reverse()
	return x


def counting(x):
	i = 0
	for j in x:
		i+=1
	return i

def deleting_values(city):
	del city[3]
	return city

def looping():
	year = [2000, 2001, 2002, 2003, 2004]
	for x in year:
		print(x)

def check():
	food = ["milk", "bread","jerky", "orange", "egg"]
	if "jerky" in food:
		return str("Match Found")

def length(n):
	return str("The length of the list is " + str(len(n)))

def multipleset():
	n = [((1, 2), (3,4)),(1, 2, 3)]
	return str(n)
	y = n[0]
	return str(y)
	x = y[0]
	return str(x)
	z = x[1]
	return str(z)

def intersection(a, b):
	a.intersection_update(b)
	return str(a)

def difference(a, b):
	c = b.difference(a)
	return str(c)

def symmetric(a, b):
	c = a.symmetric_difference(b)
	sorted(c)
	return str(c)

def unions():
	a = {1, 2, 3}
	b = {4, 5, 6}
	c = {7, 8, 9}
	d = {10, 11, 12}
	e = a.union(b, c, d)
	return str(e)

def extends():
	b = ["True", "False"]
	a = [1, 0]
	b.extend(a)
	return str(b)

def whileloop():
	a = [1, 2, 3, 4, 5]
	i = 0
	while i<5:
		i+=2
		print(i)

def sorting(x):
	x.append(7)
	x.sort()
	return str(x)

def forloop():
	a = [1, 2, 3, 4]
	i = 0
	for i in a:
		print(i)
		i+=1










print(add())
print(remove())
print(update())
print(getvalue([1, 2, 3, 4 ,5, 6]))
print(pop_values(['a', 'b', 'c', 'd','e']))
print(reverse([1, 2, 3, 4, 5, 6, 7 ,8, 9]))
print(counting([1, 2, 3, 4, 5, 6, 7, 8]))
print(deleting_values(["Philippines", "Japan", "USA", "Russia", "China"]))
looping()
print(check())
print(length([1, 2, 3, 4, 5, 6]))
print(multipleset())
print(intersection({"a", "b", "c", "d"}, {"a", "d", "f"}))
print(difference({"a", "b", "c", "d"}, {"a", "d", "f"}))
print(symmetric({"a", "b", "c", "d"}, {"a", "d", "f"}))
print(unions())
print(extends())
whileloop()
print(sorting([8, 4, 5, 6]))
forloop()
