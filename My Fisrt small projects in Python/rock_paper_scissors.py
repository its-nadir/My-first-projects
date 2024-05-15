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
game_images = [rock, paper, scissors]
def pc():
  return random.randint(0, 2)
choice=int(input("what do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
pc_choice = pc()
if  choice>=3 or choice <0 :
   print("Sorry, it's invalid choice")
else :
    print(game_images[choice])
    print("Computer chose:/n")
    print(game_images[pc_choice])  
    if choice==0 and pc_choice== 2:
         print("You win!")
    elif choice==2 and pc_choice== 0:
         print("You lose")
    elif choice < pc_choice :
         print("You lose")
    elif choice > pc_choice :
         print("You win!")
    else  :
           print("It's a draw")   

   


