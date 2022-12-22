name=input("Enter your name: ")
print("Hello",name,"Welcome to number guess game!\nThis program is made for guessing the number that is in your mind")
print("Press \'y\' for yes and \'n\' for no.\n")
number_of_guesses=int(input("Tell me how many guesses should I have: "))
print("Let think a number between 1 to 100\n")
first_num=1
mid_num=50
last_num=100

while True:
    if True:
        print("Is your number is",mid_num)
        while True:
            answer=input("Yes or No? ")
            if answer=='y' or answer=='n':
                break
            else:
                print("Please enter either y or n.\n")
        if answer=='y' or answer=='Y':
            print("I guess your number with",number_of_guesses,"guess left")
            break
        else:
            answer=='N' or answer=='n'
            number_of_guesses = number_of_guesses - 1
            if number_of_guesses == 0:
                print("I lost as no more guesses left !")
                break
            print("Now I have",number_of_guesses,"guesses left\n")
            pass
        if True:
            print("Is your number is greater than",mid_num,"?")
            while True:
                answer = input("Yes or No? ")
                if answer == 'y' or answer == 'Y':
                    first_num=mid_num
                    mid_num=int((mid_num+last_num)/2)
                    break
                elif answer == 'N' or answer == 'n':
                    last_num=mid_num
                    mid_num=int((first_num+mid_num)/2)
                    break
                else:
                    print("Please enter either y or n.\n")