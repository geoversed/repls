import random

class Adventurer:
    def __init__(self, name, health=100000, attack=100, defense=500):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        enemy.health -= abs(damage)
        return damage

    def heal(self):
        healing_power = random.randint(5, 2000)
        self.health += healing_power
        return healing_power

    def increase_defense(self):
        defense_boost = random.randint(1, 5550)
        self.defense += defense_boost
        return defense_boost

    def engage_combat(self, enemy):
        print(f"{self.name} engages in combat with {enemy.name}.")
        while self.health > 0 and enemy.health > 0:
            print(f"{self.name}'s Health: {self.health:,} | {enemy.name:}'s Health: {enemy.health:,}")
            action = input("Choose your action (1: Attack, 2: Heal, 3: Increase Defense): ")

            if action == '1':
                damage_dealt = self.attack_enemy(enemy)
                print(f"{self.name} attacks {enemy.name} and deals {abs(damage_dealt):,} damage.")
            elif action == '2':
                healing_power = self.heal()
                print(f"{self.name} heals for {healing_power:,} health.")
            elif action == '3':
                defense_boost = self.increase_defense()
                print(f"{self.name} increases defense by {defense_boost:,}.")
            else:
                print("Invalid action. Try again.")

            # Enemy's turn
            enemy_damage = random.randint(30, 3000)
            self.health -= enemy_damage
            print(f"{enemy.name} attacks {self.name} and deals {enemy_damage:,} damage.")

        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} defeats {enemy.name}!")

class Enemy:
    def __init__(self, name, health=1000000, attack=8000, defense=3000):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

# Example usage:
player = Adventurer("Hero")
enemy = Enemy("Evil Goblin")

player.engage_combat(enemy)
