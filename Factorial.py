# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("enter any number:"))
# print(factorial(num))

# n=int(input("Enter any number for finding factorial of: "))
# fac=1
# if n == 0:
#     print(fac)
# else:
#     for i in range(n):
#         fac=fac*(i+1)
#     print(f"={fac} ")

# Another method
# x=int(input("Enter any number: "))
# l=[]
# if x==0:
#     print(f"The factorial of {x} is: 1")
# else:
#     for i in range(1,x+1):
#         if i == 1:
#             a=i*i
#         else:
#             a=a*i
#         l.append(str(i))
#     l="*".join(l)
#     print(f"{l} = {a}")
#     print(f"The factorial of {x} is: {a}")