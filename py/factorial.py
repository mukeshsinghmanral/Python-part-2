n=int(input('enter natural number: '))
def fact(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	print('factorial of',n,'is:',fact)	
fact(n)