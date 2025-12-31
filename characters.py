from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, attack, hp, defense):
        self.name = name
        self.attack = attack
        self.max_hp = hp
        self.hp = hp
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def attack_target(self, target):
        dmg = target.take_damage(self.attack)
        print(f"{self.name} attacks {target.name} for {dmg} damage.")

    def take_damage(self, dmg):
        damage_actual = max(0, dmg - self.defense)
        self.hp = max(0, self.hp - damage_actual)
        print(f"{self.name} took {damage_actual} damage (HP: {self.hp}/{self.max_hp})")
        return damage_actual

    @abstractmethod
    def special_power(self, target):
        pass


class Knight(Character):
    def __init__(self, name="Knight"):
        super().__init__(name, attack=15, hp=75, defense=10)

    def special_power(self, target):
        dmg = target.take_damage(2 * self.attack)
        print(f"{self.name} uses HEAVY STRIKE on {target.name} for {dmg} damage!")


class Goblin(Character):
    def __init__(self, name = "Goblin"):
        super().__init__(name, attack=5, hp=30, defense=5)

    def special_power(self, target):
        dmg = target.take_damage(self.attack)
        self.hp = min(self.max_hp, self.hp + 5)
        print(f"Goblin uses STEAL for {dmg} damage and heals to {self.hp}/{self.max_hp} HP!")

class Golem(Character):
    def __init__(self,name = "Golem"):
        super().__init__(name, attack = 5, hp = 150 ,defense = 20)

    def special_power(self, target):
        dmg = target.take_damage(self.attack)
        self.defense += 5
        print(f"The GOLEM uses special power to increase its defense to {self.defense} and inflicts an attack of {dmg}")

class Mage(Character):
    def __init__(self, name = "Mage"):
        super().__init__(name, attack = 10, hp = 50, defense = 10)
        self.mana = 20
        self.mana_max = 20

    def special_power(self, target):
        if self.mana < self.mana_max:
            print("not enough mana, wait for it to recharge")
            return 

        dmg = target.take_damage(3*self.attack)
        self.mana = 0
        print(f"{self.name} casts a ligtening blast on {target.name} and inflicts {dmg} damage")
        print(f"mana left = {self.mana}/{self.mana_max}")

    def recharge_mana(self):
        self.mana = min(self.mana_max, self.mana + 5)
        print(f"mana = {self.mana}/{self.mana_max}")
    
        if (self.mana == self.mana_max):
            print("Mana has been restored, special attack can be used now!")


