rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

list = ["Rock" , "Paper" , "Scissor"]

response = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

computer_response = list[random.randint(0 , 2)]

if response == "0":
  print(rock)
  if computer_response == "Rock":
    print("Draw")
  elif computer_response == "Paper":
    print("You Win")
  else:
    print("You lose")

elif response == "1":
  print(paper)
  if computer_response == "Rock":
    print("You Win")
  elif computer_response == "Paper":
    print("Draw")
  else:
    print("You lose")

elif response == "2":
  print(scissors)
  if computer_response == "Rock":
    print("You lose")
  elif computer_response == "Paper":
    print("You Win")
  else:
    print("Draw")





