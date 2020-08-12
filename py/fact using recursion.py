n=int(input('enter natural number: '))
def fact(n):
	if(n==0):
		return 1
	else :
		return n*fact(n-1)
factor=fact(n)
print('factorial of',n,'is: ',factor)