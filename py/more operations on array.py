from numpy import *
arr1=array([],int)
arr2=array([],int)
n=int(input('enter number of elements of 1st array: '))
for i in range(n):
	val1=int(input('enter values of 1st array: '))
	arr1=append(arr1,val1)
m=int(input('enter no. of elements of 2nd array: '))
for i in range(m):
	val2=int(input('enter values of 2nd array: '))
	arr2=append(arr2,val2)
print(arr1)
print(arr2)	
for i in range(n):
	arr3=arr1+arr2
print(arr3)
max=arr3[0]
for i in range(n):
	if max<arr3[i]:
		max=arr3[i]
print(max)		


