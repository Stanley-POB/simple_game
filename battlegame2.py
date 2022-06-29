import random

while True:
    # Wizard Character
    wizard = "Wizard"
    wizard_hp = 70
    wizard_damage = 150

    # Elf Character
    elf = "Elf"
    elf_hp = 100
    elf_damage = 100

    # Human Character
    human = "Human"
    human_hp = 150
    human_damage = 20

    # Dragon Character
    dragon = "Dragon"
    dragon_hp = 300
    dragon_damage = 50

    # My Character
    random_hp = random.randint(50, 200)
    random_damage = random.randint(50, 100)

    # Orc Character
    orc = "Orc"
    orc_hp = 200
    orc_damage = 80

    while True:
        print("----- Characters -----")
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("5) Choose name")
        print("6) Exit")

        character = input("\nChoose your option: ")

        if character == "1":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break

        if character == "2":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        if character == "3":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        if character == "4":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break

        if character == "5":
            character = input("Type your name:")
            my_hp = random_hp
            my_damage = random_damage
            break

        if character == "6":
            exit()

        else:
            print("Unknown character, please choose an option between 1 and 6")

    print("\n")
    print(f"You have chosen the {character}")
    print("----- Characteristics -----")
    print(f"HP: {my_hp}")
    print(f"Damage: {my_damage}")
    print("\n")
    # Loop to start the battle

    while True:

        dragon_hp -= my_damage
        print(f"{character} hit {dragon}")
        print(f"{dragon}'s hitpoints are now {dragon_hp}")
        print("\n")

        my_hp -= dragon_damage
        print(f"{dragon} hit {character}")
        print(f"{character}'s hitpoints are now {my_hp}")
        print("\n")

        if dragon_hp <= 0:
            print("\n")
            print("The Dragon has lost the battle")
            break

        elif my_hp <= 0:
            print("\n")
            print(f"{character} has lost the battle")
            break

    play_again = input(
        "Would you like to play again? Please enter 'yes' or 'no': ")

    if play_again == "yes":
        continue
    if play_again == "no":
        print("Thank you for playing, see you next time")
        break
    else:
        print("Sorry we did not understand what you are trying to do, try again")
