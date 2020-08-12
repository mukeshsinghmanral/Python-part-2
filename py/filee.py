f=open('Myfirst.txt','r')
f1=open('my second.txt','a')
for data in f:
	f1.write(data)
