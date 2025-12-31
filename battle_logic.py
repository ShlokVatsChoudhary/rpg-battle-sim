#battle logic
import random, time


class Battle:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 1

        # self status, indicates the current stats of the player and the villian at every turn

    def show_status(self):
        print("\n" + "=" * 50)
        print(f"TURN {self.turn}")

        print(f"{self.player.name}: HP {self.player.hp}/{self.player.max_hp}", end = "")

        if hasattr(self.player, "mana") and hasattr(self.player, "mana_max"):
            print(f"{self.player.name}: MANA {self.player.mana}/{self.player.mana_max}", end = "")
        else:
            print()

    def gain_mana(self, character, amount):
        if hasattr(character, "mana") and hasattr(character, "mana_max"):
            character.mana = min(character.mana_max, character.mana + amount)

    def can_use_special(self,character): # permission to use mana based power
        """Mage-style rule: special only when mana is FULL. Others can always special."""
        if hasattr(character, "mana") and hasattr(character, "mana_max"):
            return (character.mana == character.mana_max)
        return True

    def regeneration_special(self,character,skipped_turn):
        # +5 every turn or +15 if turn skipped
        if hasattr(character, "mana") and hasattr(character, "mana_max"):
            if skipped_turn:
                self.gain_mana(character,15)
            else:
                self.gain_mana(character,5)



    def player_turn(self):
        while (True):
            print("CHOOSE YOUR ACTION: ",
                  "1. Normal attack",
                  "2. Special ability",
                  "3. Skip turn")
            
            try:
                choice = int(input("Enter 1/2/3: ").strip())
                time.sleep(1)

                if choice not in ("1", "2", "3"):
                    print("ERROR!\nSelect from options 1/2/3!\n")
                    continue

            
                match choice:
                    case 1:
                        self.player.attack_target(self.enemy)
                        self.player.regeneration_special(self.player, skipped_turn = False)

                    case 2:
                        if not self.player.can_use_special(self.player):
                            print("Not enough mana to perform special ability")
                            continue
                        else:
                            self.player.special_power(self.enemy)
                            self.player.regeneration_special(self.player, skipped_turn = False)

                    case 3:
                        print(f"{self.player} has skipped the turn for +15 MANA...")
                        self.player.regeneration_special(self.player, skipped_turn = True)
                
            except ValueError: print("select from option 1/2/3")


    # Enemy's turn (simple probabilistic AI)

    def enemy_turn(self):
        if hasattr(self.enemy, "mana") and hasattr(self.enemy, "mana_max"):
            if self.enemy.mana < self.enemy.mana_max:

                if random.random() < 0.35:
                    self.enemy.regeneration_special(self.enemy, skipped_turn = True)
                    return
            if self.enemy.mana == self.enemy.mana_max:

                if random.random() < 0.50:
                    print(f"The {self.enemy} has chosen to SKIP")
                    self.enemy.special_power(self.player)
                    self.regeneration_special(self.enemy, skipped_turn = False)
                    return
                
        else: # default attack
            self.enemy.normal_attack(self.player)
            self.enemy.regeneration_special(self.enemy, skipped_turn = False)

    def run(self):
        time.sleep(1)
        print("⚔️--BATTLE BEGINS--⚔️")
        while self.player.is_alive() and self.enemy.is_alive():
            self.show_status()

            self.player_turn()
            if not self.enemy.is_alive():
                print(f"\n{self.enemy.name} is defeated! YOU WON!⚔️")
                return self.player

            self.enemy_turn()
            if not self.player.is_alive():
                print(f"\n{self.enemy.name} won! YOU DIED!☠️")
                return self.enemy

            self.turn += 1 