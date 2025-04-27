def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    for letter in name1 + name2:
        if letter in ("TRUE"):
            score1 += 1
    for letter in name1 + name2:
        if letter in ("LOVE"):
            score2 += 1
    print(str(score1) + str(score2))

name1 = input("Enter the first name: ").upper()
name2 = input("Enter the second name: ").upper()

calculate_love_score(name1, name2)


