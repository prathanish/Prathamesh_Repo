def game():
    print("You wake up in the middle of a magical forest")
    print("choose which path to take.")
    print("path towards the deep parts of the forest (1)")
    print("path towards a hut in the distance. (2)")

    choice1 = int(input("which path will you take: 1 or 2?: "))

    if choice1 == 1:
        print("you see a bear sleeping near a pond")
        print("you see a small dagger lying beside a tree that the bear is sleeping next to.")
        print("do you want to walk stealthily to get past the bear... (1)")
        print("do you want to walk stealthily to get the dagger ... (2)")
        
        choice2 = int(input("which path will you take: 1 or 2?: "))
        
        if choice2 == 1:
            print("You step on a dry branch...\nyou wake up the bear by accident\nthe bear chases you")
            print("you can either jump in the pond (1) or play dead (2)")

            choice3 = int(input("which path will you take: 1 or 2?: "))

            if choice3 == 1:
                print("the bear catches up to you in the pond and you die due to mauling and drowning")
            elif choice3 == 2:
                print("the bear is suspicious... of your act\n the bear decides to scratch repeatedly")
                print("you are deeply wounded but make no reaction until the bear goes away")
                print("you survive to live another day in this treacherous world...")

        elif choice2 == 2:
            print("you try to get the dagger but step on a dry branch, waking up the bear")
            print("you can still go for the dagger (2) or you can run away (1) ")
            choice4 = int(input("which path will you choose 1 or 2?: "))
            if choice4 == 1:
                print("the bear catches up to you and you get mauled to death")
            elif choice4 == 2:
                print("you get scractched by the bear's massive claw but manage to get the dagger and get to a safe distance.")
                

    elif choice1 == 2:
        print("A person asks you where are you going and offers you chips if you stay in his hut for a while.")
        print("You die of heart faliure from eating chips")
    else: 
        print("invalid input entered.")
game()
