"""
Write a program that will hold the inventory a player has in an RPG game. 
The player has the following actions: 
pick (adds an item to the inventory), 
drop (removes an item from the inventory), 
pull (outputs a random item from the inventory) 
and search (outputs all the items in the inventory).
"""
import random


class RPG:

  def __init__(self):
    self.inventory = []

  def pick(self, item_name: str):
    self.inventory.append(item_name)

  def drop(self, item_name: str):
    try:
      self.inventory.remove(item_name)
    except ValueError:
      return "You don't have this item!"

  def pull(self):
    if self.inventory:
      return random.choice(self.inventory)
    return "You have nothing!"

  def search(self):
    iterated = ", ".join(self.inventory)
    if iterated:
      return iterated
    return "You have nothing!"


# Main Program
someones_inventory = RPG()
print(someones_inventory.search())
someones_inventory.pick("sword")
print(someones_inventory.search())
print(someones_inventory.drop("saber"))
someones_inventory.pick("saber")  
print(someones_inventory.search())
print(someones_inventory.drop("saber"))



  

  

