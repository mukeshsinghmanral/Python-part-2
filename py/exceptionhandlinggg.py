a=5
b=0
try:
	print('file open')
	print(a/b)
except Exception as m:
	print(m)
finally:
	print('file closed')	
try:
	x=int(input('enter any integer: '))
	print('successfull')
except Exception:
	print('providing any other type value to integer')