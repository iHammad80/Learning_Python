import time
import random
from datetime import timedelta

def print_guess():
    print()
    print(''.join([x+" " for x in guess]))

name=input("Enter your name: ")
print(f"Welcome {name} to Hangman game:\n\nThis program will randomly generate any word and you have to guess that words in given tries.\nWrong letter will eat your 1 try while wrong vovel will eat your 2 tries.")
guesses=6
warning=3
print(f"You have {guesses} guesses in total and {warning} warnings in total\nIf you enter a letter that you already entered earlier will cost your 1 warning. If you stand with no warnings, you will loose your guess according to rules mentioned above.\nScore = number of alphabets in word + (remaining guesses * remaing warning).\n\n")
word=random.choice((open("Words.txt").readline().split()))
print(f"The word is {len(word)} letters long\n\nAnd your time starts now!")
word=word.lower()
start_time=time.monotonic()
letter_already_guessed=[]
lst=[]
for i in range(len(word)):
    lst.append("_")
print(f"The letter is: {lst}")
guess=""
while True:
    print_guess()
    print(f"You have {guesses} guesses left and {warning} warnings left.")
    x=input("Enter your guess: ")
    if x.isalpha():
        if x in letter_already_guessed:
            print("You already guessed that letter try different one: ")
            if warning>0:
                warning-=1
            else:
                print("You ran out of warnings that's why you will loose your guess!")
                if x in "aeiouAEIOU":
                    guesses -= 2
                else:
                    guesses-=1
        elif x in word:
            letter_already_guessed.append(x)
            print("Good Guess!")
            for i, j in enumerate(word): # Enumerate checks bot index and item at at index at same time here i is index and j is item at that index
                if j is x:
                    lst[i] = x
            print(lst)
        else:
            letter_already_guessed.append(x)
            print(f"The letter {x} is not in word!")
            print(lst)
            if x in "aeiouAEIOU":
                guesses-=2
            else:
                guesses-=1
    else:
        print(f"{x} is not alphabet.")
        if warning > 0:
            warning -= 1
        else:
            print("You ran out of warnings that's why you will loose your 1 guess!")
            guesses -= 1
    if guesses==0:
        print(f"\n\nYou ran out of guesses.\n\'You lost\'. The word was {word}")
        break
    else:
        if '_' not in lst:
            print(f"\n\nCongratulations! you won with {guesses} guesses left.")
            score=len(word)+(guesses*warning)
            print(f"Your score is: {score}")
            break

end_time=time.monotonic()
print(f"\nTime Taken to finish the game: {timedelta(seconds=end_time-start_time)}")
