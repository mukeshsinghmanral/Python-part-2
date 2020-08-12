n=int(input("enter any positive number: "))
sum=0
x=n
m=0
while x>0:
    m=x%10
    sum=sum+(m*m*m)
    x=x//10
if sum==n:
    print(n,"is armstrong number")
else :
    print(n,"is not armstrong number")


