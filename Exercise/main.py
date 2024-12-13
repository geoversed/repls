
# TASK 1
def count_word_frequency(words: list) -> dict:
  count = {}  #  Create an empty dictionary
  unique_words = set(words)  # Create a unique set of the original list
  for word in unique_words:  #  Iterate through the unique set
    count[word] = words.count(word)  #  Find its frequency in the original list
  return count  # Return the new dictionary with updated values


# TASK 2
def filter_dict(hash: dict, condition) -> dict:
  # Iterate through all keys and respective values only where the condition is met
  return {key: value for key, value in hash.items() if condition(key, value)}


# TASK 3
def check_same_frequency(list1: list[int], list2: list[int]) -> bool:
  # Reused previously defined functions to determine the frequency of each word
  frq_list1 = count_word_frequency(list1)
  frq_list2 = count_word_frequency(list2)
  # Check if each word frequency is the same (ie equal)
  return frq_list1 == frq_list2

# SAMPLE DATA

# the_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(count_word_frequency(the_dict))
# print(filter_dict(the_dict, lambda _, v:  v % 2 == 0))


# a = [1, 2, 2, 3, 4, 5]
# b = [2, 2, 1, 3, 4, 5]
# print(check_same_frequency(a, b))
