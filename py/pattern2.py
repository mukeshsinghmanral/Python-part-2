lis=['A','P','Q','R']
for i in range(4):
	if i==1:
		lis[i]='B'	
	elif i==2:
		lis[i]='C'
	elif i==3:
		lis[i]='D'
	for j in lis[0:4]:
		print(j,end=' ')		
	print()	