# Faulty calculator
# Answer should be wrong for following:
# 45*3=555, 56+9=77, 56/6=4
x=int(input("Enter 1st number= "))
y=int(input("Enter 2nd number= "))
z=input("Select what operation do you want to perform? *,+,-,/= ")
if x==45 and y==3 and z=='*':
    print("The answer is 555!")
elif x==56 and y==9 and z=='+':
    print("The answer is 77!")
elif x==56 and y==6 and z=='/':
    print("The answer is 4!")
elif z==('+'):
    print("The answer is ",x+y,"!")
elif z==('-'):
    print("The answer is ",x-y,"!")
elif z==('*'):
    print("The answer is ",x*y,"!")
else:
    print("The answer is ", x/y, "!")