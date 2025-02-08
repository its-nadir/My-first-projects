import random   
words = [
    "apple", "grape", "happy", "tiger", "sunny", "bread",  
    "chair", "smile", "green", "piano", "table", "ocean",  
    "cloud", "dream", "music", "zebra", "river", "flame"  
]
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]


chosen_word= random.choice(words)
space=""
for i in range(len(chosen_word)):
    space+="_ "
print(space)
game_over=False
new_space=[""]
tries=0
while not game_over:
    guessed_letter=input("Guess a letter: ")
    space=""
    for letter in chosen_word:
        if guessed_letter== letter:
            space+=guessed_letter
            new_space.append(guessed_letter)
        elif letter in new_space:
            space+=letter
        else:
            space+=("_ ")
    if guessed_letter not in chosen_word:
        tries+=1
    print(space)
    print(hangman_stages[tries])
    if "_" not in space:
        game_over=True
        print("You win")
    elif "_" in space and tries==6:
        game_over=True
        print("You lose")
    
        
            
