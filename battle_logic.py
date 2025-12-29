#battle logic
import random
import characters


class Battle:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 1

        # self status, indicates the current stats of the player and the villian at every turn

    def self_status(self):
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

    def special_power(self,character): # permission to use mana based power
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



