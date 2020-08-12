from numpy import *
mx1=matrix('1 3 4;4 5 6;6 7 8')
mx2=matrix('6 7 8;4 3 2;2 7 8')
print('matrix1: ')
print(mx1)
print('matrix2:')
print(mx2)
print('above matrices multiplication:' )
mx=mx1*mx2
print(mx)
arr1=array([[1,3,4],[4,5,6],[6,7,8]])
arr2=array([[6,7,8],[4,3,2],[2,7,8]])
print(arr1)
print()
print(arr2)
print()
arr=arr1*arr2
print('above arrays multiplication:')
print(arr)