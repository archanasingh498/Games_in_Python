import random

rock1= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#print(rock)

paper1= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_opt = "rock", "paper", "scissors"

#Write your code below this line 👇
option = input("what option do you choose? Type 0 for rock, 1 for paper, or 2 for scissors")
#print(f"computer chose: {rand_choose}")
if option == '0':
  print(f"you chose: rock {rock1}")
elif option == '1':
  print(f"you chose: paper {paper1}")
elif option == '2':
  print(f"you chose: scissors {scissors1}")


rand_choose = random.choice(game_opt)
#print(rand_choose)

print(f"computer chose: {rand_choose}")
if rand_choose == "rock":
  print(rock1)
elif rand_choose == "paper":
  print(paper1)
elif rand_choose == "scissors":
  print(scissors1)
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

if option == '0' and rand_choose == 'scissors':
  print("You won!!")
elif option == '2' and rand_choose == 'rock':
  print("You lose!!")
elif option == '2' and rand_choose == 'paper':
  print("You won!!")
elif option == '1' and rand_choose == 'scissors':
  print("You lose!!")
elif option == '1' and rand_choose == 'rock':
  print("You won!!")
elif option == '0' and rand_choose == 'paper':
  print("You lose!!")
elif option == '0' and rand_choose == 'rock':
  print("Draw Match!!")
elif option == '1' and rand_choose == 'paper':
  print("Draw Match!!")
elif option == '2' and rand_choose == 'scissors':
  print("Draw Match!!")
else:
  print("You have entered invalid input")