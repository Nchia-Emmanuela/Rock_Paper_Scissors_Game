import random
# Rock
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# the rule to play the game is simple
# Rock Wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

number = input("enter a random number:\n")
random.seed(number)
computers_choice = random.randint(0, 2)


#user's input and choice
Your_choice = int(input("what do you choose? type '0' for Rock, '1' for Paper of '2'Scissors:\n"))
if Your_choice == 0 :
    print(f"Your Choice is: {Your_choice} (Rock)\n {Rock}")
elif Your_choice == 1:
    print(f"Your Choice is: {Your_choice} (Paper)\n {Paper}")
elif Your_choice == 2:
    print(f"Your Choice is: {Your_choice} (Scissors)\n {Scissors}")
# user choice could still be gotten by using python list as illustrated bellow
# game_image = [rock, paper, scissor]
# Your_choice = int(input("what do you choose? type '0' for Rock, '1' for Paper of '2'Scissors:\n"))
# print(game_image[Your_choice])


# computers choice
# computer selects randomly based on the seed
if computers_choice == 0:
    print(f"Computer Chose : {computers_choice} (Rock) \n{Rock}")
elif computers_choice == 1:
    print(f"Computer Chose: {computers_choice} (Paper) \n{Paper}")
else:
    print(f"Computer Chose: {computers_choice} (Scissors)\n{Scissors}")
# computer choice could still be gotten using python list
# print("computer chose:")
# print("game_image[computer_choice]")


if Your_choice >=3 or Your_choice < 0:
    print("You typed an invalid number, You Lose!!")
elif Your_choice == 0 and computers_choice == 2:
    print("You Win!!")
elif computers_choice == 0 and Your_choice == 2:
    print(" You Lose!")
elif computers_choice > Your_choice:
    print("You Lose!")
elif Your_choice > computers_choice:
    print("You Win!")
elif computers_choice == Your_choice:
    print("it is a draw!")
