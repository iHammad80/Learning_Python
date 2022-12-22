# Files IO Basics
"""
"r" - Open file for reading
"w" - Open file for Writing
"x" - Create file for not exist file
"a" - Add more content to the end of the file (a=append)
"t" - Text mode
"b" - Binary mode
"+" - read and write

"""
# f= open("Intro.txt","rt")
# x=f.read()
# print(x)

# Methods of printing
rounds=input(":")
me="Maaz"
print("Total rounds were:",rounds,me)
print("Total rounds were: {1} {0}".format(rounds,me))
print(f"Total rounds were: {rounds} {me}")