from random import randint
from typing import Literal, Optional

class Character:

  """An abstract base class where all instances of characters inherit from.
     Baseline operations common amongst all instances are included."""

  
  def __init__(self, name: str, attack: int) -> None:
    self.name: str = name
    self.health: int = 10
    self.attack: int = attack
    self.endurance: int = 0

  def perform_action(self, user, mode: Optional[Literal["atk", "def", "heal"]]):
    if isinstance(user, Character):
      if mode is None or mode == "atk":
        mode = "atk"
        user.health -= self.attack
        print(f"{self.name} just dealt {self.attack} to {user.name}.\n" 
              f"{user.name} now has {user.health} remaining")
        if user.health <= 0:
          print(f"{user.name} has been defeated! (YOU LOST!)")
      elif mode == "def":
        mode = "def"
        self.endurance += randint(1, 4)
        print(f"That's {self.endurance} defense for {self.name}!\n"
              f"Meaning attacks now deal {100-self.endurance}% HP loss "
              f"of orginal damage dealt.")
      else:
        mode = "heal"
        hpi = randint(1, 7)
        print(f"{self.name} just gained {hpi} health.\n"
              f"{self.name} now has {self.health} remaining")
  
  # Create operations that all character instances have in common
        

class Protagonist(Character):
  
  """Represents the main playable character of the RPG and 
     their operations."""
  
  all_av_items = {"Spear", "Healing Potion", ""}  # sets are optimised for mem
  
  def __init__(self, name: str, attack: int, coins: int):
    super().__init__(name, attack)
    self.coins: int = coins
    self.items = set()  # sets are faster to access and operate on than lists
  
  def add_item(self, item_name):
    if item_name in Protagonist.all_av_items:
      self.items.add(item_name)
      
  def remove_item(self, item_name):
    if item_name in Protagonist.all_av_items:
      self.items.remove(item_name)

  def perform_action(self, user, mode: Optional[Literal["atk", "def", "heal"]]):
    if isinstance(user, Character):
      if mode is None or mode == "atk":
        mode = "atk"
        user.health -= self.attack
        print(f"{self.name} just dealt {self.attack} to {user.name}.\n" 
              f"{user.name} now has {user.health} remaining")
        if isinstance(self, Protagonist) and user.health <= 0:
          reward = randint(50, 75)
          self.coins += reward
          print("YOU DEFEATED THE ENEMY!!\n"
                "- Your efforts have been acknowledged and celestia has granted"
                " you {0} coins!\n"
                "- You now have {1} coins in total.".format(reward, self.coins))
      elif mode == "def":
        mode = "def"
        self.endurance += randint(1, 49)
        print(f"That's {self.endurance} defense for {self.name}!\n"
              f"Meaning attacks now deal {100-self.endurance}% less damage.")
      else:
        mode = "heal"
        hpi = randint(1, 7)
        print(f"{self.name} just gained {hpi} health.\n"
              f"{self.name} now has {self.health} remaining")
joe = Character("Joe Biden", randint(3, 5))
george = Protagonist(name="George Washington", attack=randint(4, 60), coins=0)

george.perform_action(joe, "def")

