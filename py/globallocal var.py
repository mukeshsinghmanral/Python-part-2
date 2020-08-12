import check
a=20
def fun(): 	
	globals()['a']=8
	print(globals()['a'])
	a=30
	print(a)	
fun()
print(a)
def fin():
	print(a)
fin()	
print(__name__)