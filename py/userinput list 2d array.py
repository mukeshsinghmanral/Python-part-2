r=int(input('enter the no. of rows: '))
c=int(input('enter the no. of coloumns: '))
matrix=[]
a=[]
print('enter the enteries rowies: ')
for i in range(r):
	for j in range(c):
		a.append(int(input()))
	matrix.append(a)
for i in range(r):
	for j in range(c):
		print(matrix[i][j],end=' ')
	print()	