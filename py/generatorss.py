
def square():
	for n in range(1,11):
		sq=n*n
		yield sq
value=square()
for i in value:
	print(i)

