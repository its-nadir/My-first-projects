import random
def pc():
  return random.randint(0, 2)
choice=int(input("what do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
pc_choice = pc()
if choice==0 :
   if pc_choice==0 :
    print("Draw")
   elif pc_choice==1 :
    print("You lost")
   else :
    print("You won")
elif choice==1 :
   if pc_choice==1 :
    print("Draw")
   elif pc_choice==2 :
    print("You lost")
   else :
    print("You won")
else :
    if pc_choice==2 :
    print("Draw")
    elif pc_choice==0 :
    print("You lost")
    else :
    print("You won")
   


