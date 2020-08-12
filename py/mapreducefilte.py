from functools import reduce
l=[3,4,5,6,8,3,4,6,87,65,44]
filte=list(filter(lambda n:n%2==0,l))
doubles=list(map(lambda n : n*2,filte))
reduc=reduce(lambda a,b:a+b,doubles)
print(filte)
print(doubles)
print(reduc)