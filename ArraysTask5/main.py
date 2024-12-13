# Arrays and Lists
Pocket = []

"""
Global stmt is used in every function
because this variable is defined in
the global scope, not the enclosing scope
"""

# Subroutine to put data into the list
def PutInPocket(Item):
  global Pocket
  Pocket.append(Item)

# Subroutine to remove data from the list
def TakeOutOfPocket(Item):
  global Pocket
  Pocket.remove(Item)

# Subroutine to output the list
def ShowPocket():
  global Pocket

  # Iterate using a for loop
  for Item in Pocket:
    print(Item)


# Main program
PutInPocket("Wallet")
PutInPocket("Keys")
PutInPocket("Tissue")
TakeOutOfPocket("Keys")

ShowPocket()