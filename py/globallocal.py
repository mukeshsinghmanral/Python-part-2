a=20
def fun(): 	
	globals()['a']=8
	print(globals()['a'])
	a=30
	print(a)	
def fin():
	print(a)
if __name__=='__main__':
	fun()
	fin()
x=44
print(x.__add__(6))	