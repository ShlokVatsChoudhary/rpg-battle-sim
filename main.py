from characters import Knight, Mage, Goblin, Golem
from battle_logic import Battle
import random,time


while(True):
    print("*"*15 + " ⚔️ RPG BATTLE SIMULATOR ⚔️ " + "*"*15, end = "\n\n")
    print("Welcome hero...")
    print("please select a hero to begin the battle")
    heroes = {1: Knight,
              2: Mage
              }
    
    for key,hero in heroes.items():
        print(f"{key} : {hero}")
    time.sleep(1)

    while(True):
        try: 
            choice_hero = int(input("select 1/2 --> ").strip())

            if choice_hero not in (1,2):
                print("invalid...")
                continue

            else:
                print(f"The Hero selected is \n ⚜️  {heroes[choice_hero]} ⚜️")
                break

        except ValueError: 
            print("please select from only (1 or 2): ")

    villians = {1: Goblin,
                2: Golem
              }
    
    choice_villain = random.choice((1,2))

    print("The villian is :", end = " ")
    time.sleep(1)
    print(villians[choice_villain].__name__ + " ☠️")

    player = heroes[choice_hero]()
    enemy = choice_villain(f"{villians.get(choice_villain)}")

    battle = Battle(player,enemy)

    battle.run()

    again_play = input("Do you wish to play again? (y/n)").strip().lower()

    if again_play != "y" or again_play != "yes":
        print("THX for playing") 
        break
    else: continue

    



