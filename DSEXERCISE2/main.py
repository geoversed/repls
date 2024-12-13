import random
from pprinting import bcolors
from pprint import pprint

"""Number 1."""
numbers = [18, 2, 14, 6, 21, 8]

def reverso_average(iterable: list[int]) -> str | None | int:
  """Reverses a list, returns the total of all the numbers and the average."""
  total = 0
  iterable.reverse()
  for x in range(len(iterable)):
    total += iterable[x]
    print(iterable[x])
  avg = total / len(iterable)
  print(f"Total: {total}")
  print(f"Average: {avg}")

reverso_average(numbers)


"""Number 3."""

Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [5, 8, 3, 6]
Outlet3Sales = Outlet1Sales.copy() # [10, 12, 15, 10]

def calculate_sales_per_quarter() -> None | str | int:
  """Calculate sales for each individual quarter in each outlet."""
  respective_quarters = []
  for x in range(4):
    one = Outlet1Sales[x]
    two = Outlet2Sales[x]
    three = Outlet3Sales[x]
    total_qtr = one+two+three
    respective_quarters.append(total_qtr)

  for x in range(len(respective_quarters)):
    print(f"Total for quarter {x+1} is {respective_quarters[x]}")

# calculate_sales_per_quarter()


"""Number 4."""
def calc_sales_per_outlet() -> None | str | int:
  """Calculate sales for each individual quarter, but in 50 different outlets"""
  outletSalesAll = []
  outletSalesQtr = [0, 0, 0, 0]
  for x in range(50):
    sales_indivOutlet = [random.randint(x+1, 50) for i in range(4)]
    outletSalesAll.append(sales_indivOutlet)
  for outlet in range(50):
    for quarter in range(4):
      outletSalesQtr[quarter] += outletSalesAll[outlet][quarter]
  for x in range(len(outletSalesQtr)):
    print(f"Total for quarter {x+1} {outletSalesQtr[x]}")

# calc_sales_per_outlet()


"""Number 5."""

def tictactoe():
  # Create a 2D grid
  grid = [['x' for _ in range(4)] for _ in range(6)] # initializes all elements to 'x'
  
  
  character_row = 0 # initial position of the character is set to the top-left corner
  character_col = 0
  
  # Function to print the grid
  def print_grid(): # function is defined to print the current state of the grid.
      for row in grid: # # nested loop + traverse 2D grid + show on console
          print(" ".join(row))
  
  # Main game loop
  while True:  # enters an infinite loop, continues until user types 'stop' to exit.
      print_grid()
      try:  # try clause used respond to any error calls
          row = input("Enter a row (1-6): ") # prompts user to enter a row and column
          if row.lower() == 'stop':
              print("Game has ended.")
              break
          col = input("Enter a column (1-4): ")
          if col.lower() == 'stop':
                print("Game has ended.")
                break
          if 1 <= int(row) <= 6 and 1 <= int(row) <= 4: # check if the inputs are valid
              grid[character_row][character_col] = 'x' # attempts to pass into row + col
              character_row = int(row) - 1 # update user pos, based on zero-indexed lists
              character_col = int(row) - 1
              grid[character_row][character_col] = 'O' # placeholder to replace old pos
          else:
              print("Invalid coordinates. Please enter valid values.") # range check
      except ValueError:
          print("Please enter valid row and column values.") # format check

# tictactoe()


"""Number 6."""

def car_park_init():
  # max column length is 6 len()
  # 10 rows, 6 columns
  permitted = False
  parking_slots = [['empty' for _ in range(6)] for _ in range(10)]
  reg_no = input("Enter car registration number: ")
  
  print(f"{bcolors.HEADER}Enter row and column of car"
        f"location SEPERATED BY A SPACE.\n"
        f"Example: 2 5 (2 is the row, 5 is the column)\n")

  ref = input(f"{bcolors.WARNING}Reference: ").split(' ')
  try:
    row, col = int(ref[0]), int(ref[1])
  except ValueError:
    print("reference number cannot be a string!")
    exit(404)
  if 1 <= int(row) <= 10 and 1 <= int(col) <= 6:
    if parking_slots[row-1][col-1] == "empty":
      permitted = True
      parking_slots[row-1][col-1] = reg_no
    else:
      print(f"{bcolors.FAIL} That space is taken")
  else:
      print(f"{bcolors.WARNING} Invalid ref.")
      permitted = False
    
  while len(ref) != 2 or not(permitted):
    print(f"{bcolors.FAIL}An error occured. Possible reasons include:\n"
          "-> Invalid reference number\n"
          "-> The reference number input was already taken\n"
          "Please try again.")
    ref = input(f"{bcolors.WARNING}Reference: ").split(' ')

  print(f"{bcolors.OKGREEN}You have been registered in the parking lot.\n\n")
  print(pprint(parking_slots, depth=4))
    

# car_park_init()

"""This is the end of the exercise."""