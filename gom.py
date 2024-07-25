import random

def start_game():
    print("gomblems")
    yes()

def yes():
    print("\nDo you want to play?")
    choice = input("Type 'yes', 'no', or 'about': ").lower()

    if choice == "yes":
        start()
    elif choice == "no":
        end_game()
    elif choice == "about":
        about()
    else:
        print("Invalid choice. Please type 'yes', 'no', or 'about'.")
        yes()

def about():
    print("This game was made by John or JTGG64 in 2024.")
    choice = input("Type 'back' to return: ").lower()
    
    if choice == "back":
        yes()
    else:
        print("Invalid choice. Please type 'back'.")
        about()

def start():
    print("\nStarting the game...")
    starting()

def starting():
    print("\nWelcome to Gomblems. This is a text-based game.")
    print("Go to Mr. Tor by typing 'mr.tor' to learn about the game.")
    print("If you have played this game before, type 'just play now'.")
    
    choice = input("Type 'mr.tor' or 'just play now': ").lower()
    
    if choice == "mr.tor":
        mr()
    elif choice == "just play now":
        play()
    else:
        print("Invalid choice. Please type 'mr.tor' or 'just play now'.")
        starting()

def mr():
    print("\nHello, this is Mr. Tor. Welcome to the game. Explore and have fun!")
    play()

def play():
    print("\nYou're in %%$64. Type 'walk' to explore.")
    walk()

def walk():
    print("\nType 'walk' to explore or 'stop' to end the game.")
    choice = input("Type 'walk' or 'stop': ").lower()

    if choice == "walk":
        if random.random() < 0.35:  # 35% chance to encounter a monster
            monster()
        else:
            print("\nYou are walking safely...")
            walk()
    elif choice == "stop":
        end_game()
    else:
        print("Invalid choice. Please type 'walk' or 'stop'.")
        walk()

def monster():
    print("\nA wild monster appears!")
    walk_or_fight()

def walk_or_fight():
    print("\nDo you want to 'fight' the monster or 'run'?")
    choice = input("Type 'fight' or 'run': ").lower()

    if choice == "fight":
        print("\nYou fight the monster and win!")
        walk()
    elif choice == "run":
        print("\nYou run away safely.")
        walk()
    else:
        print("Invalid choice. Please type 'fight' or 'run'.")
        walk_or_fight()

def end_game():
    print("\nSorry you don't want to play. Goodbye!")

if __name__ == "__main__":
    start_game()