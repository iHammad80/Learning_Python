import random

print("Welcome to Snake, Water and Gun game:\n\nRules are following:\n\nSnake vs. Water: Snake drinks the water hence wins.\nWater vs. Gun: The gun will drown in water, hence a point for water\nGun vs. Snake: Gun will kill the snake and win\n\nIn situations where both players choose the same object, the result will be a draw..\nPress s for Snake\n      w for Water\n      g for Gun.\n")
n=int(input("How many rounds you want to play: "))
rounds=1
computer_win=0
player_win=0
draw=0
lst=["Snake","Water","Gun"]

while rounds<=n:
    computer_choice = random.choice(lst)
    player_choice = input("Enter your choice: ")
    while True:
        if player_choice == 's':
            a = "Snake"
            break
        elif player_choice == 'w':
            b = "Water"
            break
        elif player_choice == 'g':
            c = "Gun"
            break
        else:
            print("Please press s, w or g:")
            player_choice = input("Press again: ")

    if computer_choice=="Snake":
        if player_choice=='s':
            print(f"Computer choice was {computer_choice}\nYour choice was {a}\nMatch Draw!\n")
            draw+=1
        elif player_choice=='w':
            print(f"Computer choice was {computer_choice}\nYour choice was {b}\nComputer Wins!\n")
            computer_win+=1
        else:
            print(f"Computer choice was {computer_choice}\nYour choice was {c}\nPlayer Wins!\n")
            player_win+=1
    if computer_choice=="Water":
        if player_choice=='s':
            print(f"Computer choice was {computer_choice}\nYour choice was {a}\nPlayer Wins!\n")
            player_win+=1
        elif player_choice=='w':
            print(f"Computer choice was {computer_choice}\nYour choice was {b}\nMatch Draw!\n")
            draw+=1
        else:
            print(f"Computer choice was {computer_choice}\nYour choice was {c}\nComputer Wins!\n")
            computer_win += 1
    if computer_choice=="Gun":
        if player_choice == 's':
            print(f"Computer choice was {computer_choice}\nYour choice was {a}\nComputer Wins!\n")
            computer_win += 1
        elif player_choice == 'w':
            print(f"Computer choice was {computer_choice}\nYour choice was {b}\nPlayer Wins!\n")
            player_win+=1
        else:
            print(f"Computer choice was {computer_choice}\nYour choice was {c}\nMatch Draw!\n")
            draw+=1
    rounds+=1

print(f"Total rounds were: {rounds-1}")
if computer_win>player_win:
    print(f"Computer won {computer_win} times, you won {player_win} times and tie {draw} times.\nYou lost. Better luck next time!")
elif computer_win<player_win:
    print(f"Computer won {computer_win} times, you won {player_win} times and tie {draw } times.\nYou win. Congratulations!")
else:
    print(f"Computer won {computer_win} times, you won {player_win} times and tie {draw} times.\nMatch Draw!")