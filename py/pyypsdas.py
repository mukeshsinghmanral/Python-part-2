from numpy import *
arr=array([[],[]])
r=int(input('enter no.of rows: '))
c=int(input('enter no. of coloumns: '))
print('enter values : ')
for i in range(r):
	for j in range(c):
		arr=append(arr,int(input()))
	print()
print("array is : ")	
for i in range(r):
	for j in range(c):
		print(arr[i][j],end=' ')
	print()