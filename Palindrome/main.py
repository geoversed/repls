# Importing the Stack class from stack_abc module
from stack_abc import Stack


# Function to check if a given word is a palindrome
def is_palindrome(word):
    # Converting the word to lowercase for case-insensitive comparison
    word_mod = word.lower()

    # Creating an instance of the Stack class
    stack = Stack()

    # Pushing each letter of the word onto the stack
    for letter in word_mod:
        stack.push(letter)

    # Reversing the word using the stack
    reverse_word = ""
    while not stack.isEmpty():
        reverse_word += stack.pop()

    # Checking if the original word is equal to its reverse
    res = bool(word_mod == reverse_word)

    # Using a match statement for more concise code
    match res:
        case True:
            nr = "\"{0}\" is a palindrome".format(word)
        case False:
            nr = "\"{0}\" is not a palindrome".format(word)

    # Returning the result message
    return nr

# Testing the function with different words
def use_test_data():
  while True:
    word = input("Enter a word to test (type \"exit\" to leave): ")
    if word == "" or word == "exit":
      match word:
        case "":  
          print("No word has been entered. Try again.\n")
        case _:
          print("Successfully quit the operation.")
          exit(101)
      continue
    else:
      print(is_palindrome(word))
      print("\n")


# Calling the use_test_data function to test the function with different words
use_test_data()