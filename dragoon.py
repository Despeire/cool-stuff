def dragon_game():
    print("You discover a cave and decide to go in (you aren't particularly smart)\n")
    print("OH NO! You find yourself in front of a huge dragon looming over you\n")

    print("What do you do?")
    print("1: Fight the dragon")
    print("2: Bait the dragon with meat and then run")
    print("3: Run away")
    print("4: Befriend the dragon\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nYou bravely fight the dragon... but it breathes fire and you die.")
    elif choice == "2":
        print("\nYou throw some meat to distract the dragon and make a run for it. You escape safely!")
        print("While running, you find a fork in the cave's road.")
        print("1: Take the left path")
        print("2: Take the right path\n")
        
        fork_choice = input("Enter the number of your choice: ")
        if fork_choice == "1":
            print("\nYou take the left path, but unfortunately, you fall into a hidden hole and die.")
        elif fork_choice == "2":
            print("\nYou take the right path and find a treasure chest filled with gold and jewels!")
            print("You also find the cave's exit and escape triumphantly!")
        else:
            print("\nIndecision gets the better of you, and you wander aimlessly until the dragon finds and eats you.")
    elif choice == "3":
        print("\nYou try to run away, but the dragon quickly chases you down and you die.")
    elif choice == "4":
        print("\nYou approach the dragon with intent to befriend it. Surprisingly, it decides 'why not.'\n")
        print("Congratulations, you've created a new timeline where you and the dragon become allies!\n")
        print("The dragon helps you out of the cave, and together you find a three-way fork in the road.")
        print("1: Head North")
        print("2: Head East")
        print("3: Head West\n")

        fork_choice = input("Enter the number of your choice: ")

        if fork_choice == "1":
            print("\nYou head north and encounter a witch.")
            print("1: Try to fight her")
            print("2: Attempt to reason with her")
            print("3: Run away")
            print("4: Do nothing\n")

            witch_choice = input("Enter the number of your choice: ")
            if witch_choice == "1":
                print("\nYou try to fight the witch, but she turns you into a frog and you die.")
            elif witch_choice == "2":
                print("\nYou attempt to reason with the witch, but she curses you to eternal pain. You die.")
            elif witch_choice == "3":
                print("\nYou try to run away, but she summons a storm that strikes you down. You die.")
            elif witch_choice == "4":
                print("\nYou do nothing, and the witch disintegrates you with a spell. You die.")
            else:
                print("\nIndecision is not an option with the witch. You die.")

        elif fork_choice == "2":
            print("\nYou head east and find a kingdom.")
            print("You and the dragon terrorize the population, becoming feared legends in the land!")

        elif fork_choice == "3":
            print("\nYou head west and encounter a gnome who needs your help.")
            print("The gnome looks at you and says, 'I have a quest for you, but that's a story for another time!'")
        else:
            print("\nIndecision leads you and the dragon in circles until you both die of boredom.")
    else:
        print("\nThe dragon is confused by your indecisiveness and decides to eat you.")

# Start the game
dragon_game()
