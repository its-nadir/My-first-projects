line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") 
indices = {'A': 0, 'B': 1, 'C': 2}
y=indices[position[0].upper()] 
x=int(position[1])-1
map[x][y]="X"
print(f"{line1}\n{line2}\n{line3}")
