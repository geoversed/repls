from typing import Literal

# Operations on Tuples based on the following
# Find it on teams, it is due soon.

# Methods of creating a tuple
tu = tuple("hi")
tu = ("hi",)  # include comma for 1 val only
tu = ("hi", "hello")  # for >1 vals

# Performing operations on tuples
for item in tu:
  print(item[-1])  # last letter of each item
  print(item[:2])  # first 2 letters of each item
  print(item[::])  # equal to item w/ no slicing
  
k = sorted(tu)  # sorts the tuple
print(f"{k}- sorted\n{tu} - original")  # prints the sorted tuple)
tu.count("hi")  # count the times hi appears

# tu[0] = "bye"  # replace first item with bye
# this will not work bc tuples are immutable datastructures

tu.index("hi")  # find the index of hi

def is_in_iterable(item, iterable: tuple, mode: Literal["manual", "auto"]):
  """Find if an element is within a collection, methods can vary."""
  match mode:
    case "auto":
      resp = item in iterable
      if resp:
        return True, f" {item} is found at index: {iterable.index(item)} "  # O(1)
      return False, 'not found'
    case "manual":
      for i in range(0, len(iterable)):  ## O(n) but len will take O(1)
          if iterable[i] == item:  # O(1)
              return True, f" {item} is found at index: {i} "  # O(1)
      return False, 'not found'  # O(1)
    case _:
      return "Not a valid query."

response = is_in_iterable("hi", tu, "auto")
print(response)

new = ("bye", "goodbye")

combined = (new + tu)
print(combined)

double = (new * 2)  # duplicate a tuple
print(double)
print(len(double), double.__len__(), sep=' ')  # both work, do same thing

previously = ["inter", "interaction"]
converted = tuple(previously)  # casting from list -> tuple
print(previously, converted, sep=' ')

del converted # deletes the tuple entirely
