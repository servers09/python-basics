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
