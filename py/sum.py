a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
def sum(a,b=87):
    print("sum of",a, "and",b ,"is",a+b)
sum(a,b)
sum(a)