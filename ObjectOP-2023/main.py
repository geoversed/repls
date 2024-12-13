import random # importing the lib that makes random decisions

class Pokemon:  # creating the blueprint named 'Pokemon'
  def __init__(self, name: str, elementType: str): # declaring the constructor
    self.name = name # setting the attributes
    self.type = elementType
    self.hp = 100

  def hp_now(self): # method that returns an object's name + hp
    print(f"{self.name} now has {self.hp}")

  def heal(self): # method that heals the ally
    hp_restored = random.randint(1, 20)
    if self.hp == 100:
      return("you already have full hp!!")
    self.hp += hp_restored
    if self.hp > 100:
      self.hp = 100
      return(f"{self.name} has received healing, restored to full hp!!")
    else:
      return(f"{hp_restored}HP restored from healing.")
      
  def attack(self, enemy, dmg): # method to attack an object
    print(f"The {self.name} attacks!")
    new_hp = enemy.hp - dmg
    enemy.hp = new_hp
  
bulbasaur = Pokemon("Bulbasaur", "Grass") # creating our objects
squirtle = Pokemon('Squirtle', "Water") # aka. instantiation
charmander = Pokemon("Charmander", "Fire")
gemtri = Pokemon("Gemtry", "Earth")

pokeList = [bulbasaur, squirtle, charmander, gemtri]

def simpleBattle():
  print("Trainer has asked to battle.")

  enemy = random.choice(pokeList)
  pokeList.remove(enemy)
  player = random.choice(pokeList)

  while enemy.hp > 0: # retain state of battle until enemy is dead
    move = input("""choose a move between 1, 2 and 3 inclusive:\n
    1. Attack the enemy\n2.Stronger attack to enemy\n3.Heal yourself""")
    if move == "1":
      player.attack(enemy, 10) # deals small damage to the enemy
      enemy.hp_now() # return enemy name and hp
    elif move == "2": 
      player.attack(enemy, 40) # deals big damage to the enemy
      enemy.hp_now() # return enemy name and hp
    elif move == "3":
      response = player.heal()
      print(response) # returns heal amount and new hp of ally
    else:
      print("invalid choice") # exception handler
  print("The enemy {0} has fainted.".format(enemy.name)) 

simpleBattle()