a=int(input("enter 1st no."))
b=int(input("enter 2nd no"))
print("initially a=",a,"b=",b)
def swap(x,y):
    x, y = y, x
    return x ,y
a,b=swap(a,b)
print("after swapping a=",a,"b=",b)