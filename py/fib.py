def fib(n):
	''' this is to find fibonacci series upto some limit'''
	a,b=0,1		
	print("fibonacii series of",n,"terms is :",end=' ')
	print(a ,b ,end=' ')
	for i in range(n-2):	
		c=a+b
		print(c,end=' ')
		a=b				
		b=c
try:								
	n=int(input('enter number of terms: '))
	if n==1:
		print(0)
	elif n<=0:
		print('invalid number of terms!')
	else:
		fib(n)
except Exception:
	print('ENTER A INTEGER TYPE VALUE.\nDON\'T YOU GET IT!!')	