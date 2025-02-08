import random
print("Rock paper scissors GO!")
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    else: print("invalid input entered")

print("Computer's turn: Rock(r) Paper(p) or Scissors(s)? \n")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you = input("Your turn: Rock(r) Paper(p) or Scissors(s)? \n")

a = gameWin(comp, you)

if comp == 'p':
    print("Computer chose paper...")
elif comp == 's':
    print("Computer chose scissors...")
else:
    print("Computer chose rock...")

if you == 'p':
    print("You chose paper...")
elif you == 's':
    print("You chose scissors...")
elif you == 'r':
    print("You chose rock...")
else:
    print("invalid input entered")


if a == None:
    print("This game is a tie!")
elif a == True:
    print("You win!")
elif a == False:
    print("You lose :(")
