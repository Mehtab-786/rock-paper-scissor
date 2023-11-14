import random

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


image = [rock,paper,scissors]
name = ["rock","paper","scissor"]

your_turn = int(input("choose 0 for rock,1 for  paper or 2 for scissor :"))
print(name[your_turn])
print(image[your_turn])

computer_turn = random.randint(0, 2)
print(name[computer_turn])
print(image[computer_turn],'\n\n')


if your_turn == 0 and computer_turn == 2:
    print('You win')
elif your_turn == 2 and computer_turn == 0:
    print('You lose')
elif your_turn > computer_turn:
    print("You win")
elif your_turn < computer_turn:
    print("You Lose")
elif your_turn == computer_turn:
    print("Draw")
