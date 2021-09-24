import random
import os

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
game_images = [rock, paper, scissors]
response = [0, 1, 2]

def rpc():
  try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  except ValueError:
    print("This is not a number, please try again !")
    rpc()
  else:
    if user_choice not in response:
        print("You typed an invalid number, you lose!")
        choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])


        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
            choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
        elif computer_choice > user_choice:
            print("You lose")
            choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
        elif user_choice > computer_choice:
            print("You win!")
            choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
        elif computer_choice == user_choice:
            print("It's a draw")
            choice = input("Do you wanna play again ? Type 'y' or 'n' ").lower()
    if choice == "y":
          os.system('clear')
          rpc()
  
rpc()