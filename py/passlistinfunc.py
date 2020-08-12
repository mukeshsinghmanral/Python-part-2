list=[]
n=int(input('enter number of elements: '))
for i in range(n):
	val=input('enter values: ')
	list.append(val)
print(list)	
def namelen(list):
	leng=0
	for i in list:
		if len(i)<=5:
			leng=leng+1
	return leng		
length=namelen(list)
print("names more than 5 letters: ",length)