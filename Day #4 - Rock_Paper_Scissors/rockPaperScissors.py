# Rock Paper Scissors
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

rock_paper_scissors = [rock, paper, scissors]
choice_list = [0, 1, 2]
computer_choice = random.choice(choice_list)

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if human_choice not in choice_list:
    print('You Lose.')
    print('Reason: FAILURE')
else:
    print(rock_paper_scissors[human_choice])
    print(f"Computer Choice: \n {rock_paper_scissors[computer_choice]}")
    if computer_choice == 0 and human_choice == 2:
        print('You Lose.')
    elif human_choice == 0 and computer_choice == 2:
        print('You Win.')
    elif human_choice > computer_choice:
        print('You Win.')
    elif human_choice > computer_choice:
        print('You Lose.')
    else:
        print('Draw')





