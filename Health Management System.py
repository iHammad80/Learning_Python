# Health Management System
# 3 clients Usman, Amin, Muaviya
# Create 6 files for each client for food and 3 for exercise
# write a function when executed takes as input client name
# Also log and retrieve data from files

import time
def gettime():
    return time.asctime(time.localtime(time.time()))

# def value_of_k(k):
#     while True:
#         if k==1 or k==2 or k==3:
#             break
#         else:
#             print("\nPlease press either 1, 2 or 3:")
#             k = int(input("Press again: "))

def log(k):
    while True:
        if k == 1:
            while True:
                c = int(input("Press 1 for food and 2 for exercise: "))
                if c == 1:
                    with open("Usman Food.txt", "a") as uf:
                        x = input("What did you eat? ")
                        uf.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                elif c == 2:
                    with open("Usman Exercise.txt", "a") as ue:
                        x = input("What exercise you recently did? ")
                        ue.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                else:
                    print("Please enter either 1 or 2 !\n")
            break
        elif k == 2:
            while True:
                c = int(input("Press 1 for food and 2 for exercise: "))
                if c == 1:
                    with open("Amin Food.txt", "a") as af:
                        x = input("What did you eat? ")
                        af.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                elif c == 2:
                    with open("Amin Exercise.txt", "a") as ae:
                        x = input("What exercise you recently did? ")
                        ae.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                else:
                    print("Please enter either 1 or 2 !\n")
            break
        elif k==3:
            while True:
                c = int(input("Press 1 for food and 2 for exercise: "))
                if c == 1:
                    with open("Muaviya Food.txt", "a") as mf:
                        x = input("What did you eat? ")
                        mf.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                elif c == 2:
                    with open("Muaviya Exercise.txt", "a") as me:
                        x = input("What exercise you recently did? ")
                        me.write(str([str(gettime())])+":"+x+"\n")
                        print("Written successfully")
                    break
                else:
                    print("Please enter either 1 or 2 !\n")
            break
        else:
            print("Please press 1, 2 or 3:")
            k=int(input("Press again: "))

def retrieve(k):
    while True:
        if k==1:
            while True:
                x=int(input("Press 1 for food, 2 for Exercise: "))
                if x==1:
                    with open ("Usman food.txt") as uf:
                        for i in uf:
                            print(i,end="")
                    break
                elif x==2:
                    with open ("Usman Exercise.txt") as ue:
                        for i in ue:
                            print(i, end="")
                    break
                else:
                    print("Please press 1 or 2: ")
            break
        elif k==2:
            while True:
                x=int(input("Press 1 for food, 2 for Exercise: "))
                if x==1:
                    with open ("Amin food.txt") as af:
                        for i in af:
                            print(i, end="")
                    break
                elif x==2:
                    with open ("Amin Exercise.txt") as ae:
                        for i in ae:
                            print(i, end="")
                    break
                else:
                    print("Please press 1 or 2: ")
            break
        elif k==3:
            while True:
                x=int(input("Press 1 for food, 2 for Exercise: "))
                if x==1:
                    with open ("Muaviya food.txt") as mf:
                        for i in mf:
                            print(i, end="")
                    break
                elif x==2:
                    with open ("Muaviya Exercise.txt") as me:
                        for i in me:
                            print(i, end="")
                    break
                else:
                    print("Please press 1 or 2: ")
            break
        else:
            print("Please press 1, 2 or 3:")
            k=int(input("Press again: "))

print("Health Management System\nThis software contains data of food and exercise for 3 clients (Usman, Amin, Muaviya). To see their data, follow these instructions. ")
m=int(input("Do you want to log or retrieve?\nPress 1 for log and 2 for retrieve: "))
while True:
    if m==1:
        k = int(input("Press 1. For Usman\n      2. For Amin\n      3. For Muaviya\n     Type here: "))
        # value_of_k(k)
        log(k)
        break
    elif m==2:
        k = int(input("Press 1. For Usman\n      2. For Amin\n      3. For Muaviya\n     Type here: "))
        # value_of_k(k)
        retrieve(k)
        break
    else:
        print("\nPlease press either 1 or 2: ")
        m=int(input("Press again: "))