"""This is Practice Exercise 6."""

# ---------------- TASK 1 ----------------


bank_holidays_in_month = [1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]

def bank_holiday(month: int) -> int:
  """Returns the number of bank holidays in a specified month."""
  if 1 > month > 12:
    raise ValueError("numerical numbers unmatching range between Jan Dec.")
  return bank_holidays_in_month[month-1]

word = bank_holiday(5)
# print(word) uncomment this to execute the task

# ---------------- TASK 2 ----------------

def my_sort(unsorted: list) -> list:
  """Sorts a list. Does not use the .sort() method"""
  shallow_copy = sorted(unsorted)
  return shallow_copy

# my_sort([2, 1, 0.1, 0.6, 6, 4, 9]) uncomment this to execute

# ---------------- TASK 3 ----------------

def discount_ten(original: list) -> list | str:
  """Returns a list that has a 10% discount of the original list that has been input."""
  discounted = []
  try:
    for element in original:
      assert type(element) == float
      new_val = 0.9 * element
      discounted.append(new_val)
    return discounted
  except Exception:
    return("invalid input type of list")

new = discount_ten([10.9, 12.6, 52.11, 76.4, 32.98])
# print(new) uncomment this to execute the task


# ---------------- TASK 4 ----------------

def add_hello(sent: list):
  """Takes a list, adds the element 'hello' to the end."""
  sent.append("hello")
  print(sent)

# add_hello(['143', 'regex', 'spacer', 'newline', 'expandtabs'])
# uncomment the above line to execute this task
  
# ---------------- TASK 5 ----------------

def remove_five(sent: list) -> list:
  """Removes all instances of the integer 5 from a given list"""
  if sent.count(5) > 0:
    for item in sent:
      if item == 5:
        sent.remove(item)
  return sent

new_list = remove_five(['HEAP', 'TSL', 'psutils', 5])
another_list = remove_five(['5', 5])
third_list = remove_five([6, 7, 8, 9])
# print(new_list, another_list, third_list, end='\n')
# uncomment the above line to execute this task

# ---------------- TASK 6 ----------------

def is_palindrome(word: str) -> bool:
  """A predicate that determines if a word is a palindrome"""
  reverse_thru_list = []
  for character in word:
    reverse_thru_list.append(character)
  reverse_thru_list.reverse()
  reversed_word = ''.join(reverse_thru_list)
  if word == reversed_word:
    return True
  return False

# if is_palindrome('a'):
#  print("this is a palindrome!")
# else:
#   print("this is not a palindrome!")
# uncomment the above 4 lines of code to execute task

# ---------------- TASK 7 ----------------

def unique_elements(type_list: list) -> list:
  """Returns a list that only contains unique elements"""
  converted = set(type_list)
  re_converted = list(converted)
  re_converted.sort()
  return re_converted

# new_made = unique_elements([1, 2, 2, 3, 3, 4])
# print(new_made)

# ---------------- TASK 8 ----------------

def backways(userl: list) -> list:
  """Takes a list and returns it in reverse order."""
  userl.reverse()
  return userl

# new_rev = backways([5, 1, 5, 8, 1, 0.5, 1])
# print(new_rev)
# uncomment the above 4 lines of code to execute task

# ---------------- TASK 9 ----------------

def sum_list(userL: list[int | float]) -> int | float:
  """Takes a list as input, sum of all elements returned."""
  the_sum = 0
  for item in userL:
    if isinstance(item, int):
      the_sum += item
      continue
    else:
      if isinstance(item, float):
        the_sum += item
      continue
  return the_sum

# the_sum = sum_list([4, 1, 6, 1, 7, 26, 69, 100])
# print(the_sum)    
# uncomment the 2 lines of code above to execute

# ---------------- TASK 10 ----------------

def mean_list(orig: list) -> int | float:
  """Takes list as input, returns the average of integers in a list."""
  total = sum_list(orig)
  mean = total/len(orig)
  return mean

# the_mean = mean_list([54, 1, 2, 512, 2451252, 6236])
# print(the_mean)
# uncomment above 2 lines to execute this task

# ---------------- TASK 11 ----------------

def list_of_deviation(input_list) -> list:
    """Find the deviation elements from the mean of input list."""
    if not input_list:
        raise ValueError("Input list is empty")

    mean = sum(input_list) / len(input_list)

    deviations = [x - mean for x in input_list]

    return deviations

# deviations = list_of_deviation([4, 1, 626, 6322492, 105])
# print(deviations)
# uncomment above 2 lines of code to execute task

# -----------------------------------------

"""This is the end of Practice Exercise 6."""