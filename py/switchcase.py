a=int(input('enter first number: '))
b=int(input('enter second number: '))
def add(a,b):
	print(a+b)
def sub(a,b):
	print(a-b)
def multi(a,b):
	print(a*b)
def div(a,b):
	print(a/b)
switcher={1: add(a,b),2: sub(a,b),3: multi(a,b),4: div(a,b)}
n=int(input('enter your choice: '))
print(switcher.get(n))			