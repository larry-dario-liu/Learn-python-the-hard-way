a = raw_input(">10 but <80-->")
def gg(a):
	i = 0
	numbers = []
	while i < int(a):
		numbers.append(i)
		i = i + 1
	print numbers
gg(a)