x=int(input("enter number of rows: "))
y=int(input("Enter either 0 or 1: "))
z=bool(y)
# For ascending order
if z==True:
    for i in range(1,x+1):
        print("*"*i)
# For descending order
else:
    for i in range(x,0,-1):
        print("*"*i)