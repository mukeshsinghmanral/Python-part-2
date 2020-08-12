def sub(a,b):
	print(a-b)
def decor(func):
	def swap(x,y):
		if x<y:
			x,y=y,x
		return func(x,y)
	return swap
sub1=decor(sub)		
sub1(23,423) #calling inner as sub1=inner 