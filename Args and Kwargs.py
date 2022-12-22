def class_data(a,b,*args,**kwargs):
    print(a)
    print(f"The teachers of this class are: {b}\n")
    print("The Students are:")
    count=1
    for i in args:
        print(f"Student {count} Name: {i}")
        count+=1
    print()
    for key,value in kwargs.items():
        print(f"Sir/Mam {key} is for subject {value}")

a=input("This data is for class: ")
teachers=[]
while True:
    choice=input(("\nDo you want to add more teachers?\nPree y for yes and n for no: "))
    if choice=='y':
        b=input("\nEnter Teacher Name: ")
        teachers.append(b)
    if choice=='n':
        print()
        break
    else:
        if choice != 'y' and choice != 'n':
            print("\nPlease enter either y or n!")
teachers_role={}
for i in teachers:
    key=i
    value=input(f"Enter role for Sir/Mam {key} : ")
    teachers_role[key]=value

students=[]
while True:
    choice = input(("\nDo you want to add more Students?\nPree y for yes and n for no: "))
    if choice == 'y':
        b = input("\nEnter Student Name: ")
        students.append(b)
    elif choice == 'n':
        break
    else:
        if choice != 'y' and choice != 'n':
            print("\nPlease enter either y or n!")

class_data(a,teachers,*students,**teachers_role)
