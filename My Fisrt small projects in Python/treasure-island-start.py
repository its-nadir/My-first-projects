print('''

  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 =input("you are on a crossroad, Do you want to go left or right?\n").lower()
if choice1 =="left":
 print("Fall into a hole. Game Over.")
elif choice1 =="right":
  choice2 =input("You have arrived at a lake. Do you want to 'wait' or 'swim'?\n").lower()
  if choice2 =="swim":
   print("Attacked by trout. Game Over.")
  elif choice2 == "wait":
    choice3 =input("Great, You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 =="red":
      print("Eaten by beasts. Game Over.")
    elif choice3  =="yellow":
      print("Burned by fire. Game Over.")
    elif choice3  =="blue":
      print('''
                          You Win!                                                                                                                          
                                                                       ,d     
                                                                       88     
 ,adPPYba,  ,adPPYba,  8b,dPPYba,   ,adPPYb,d8 8b,dPPYba, ,adPPYYba, MM88MMM  
a8"     "" a8"     "8a 88P'   `"8a a8"    `Y88 88P'   "Y8 ""     `Y8   88     
8b         8b       d8 88       88 8b       88 88         ,adPPPPP88   88     
"8a,   ,aa "8a,   ,a8" 88       88 "8a,   ,d88 88         88,    ,88   88,    
 `"Ybbd8"'  `"YbbdP"'  88       88  `"YbbdP"Y8 88         `"8bbdP"Y8   "Y888  
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
           
           ''')
    else :print("Game Over.")
      #;
 

