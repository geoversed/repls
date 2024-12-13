

def factorial(n):
  """
  Calculate the factorial of a number.
  """
  
  if n == 0 or n == 1:
    return 1
  
  else:
    return n * factorial(n - 1)

def is_strong_number(num):
  """
  Check if a number is a strong number.
  """
  
  # Convert the number to a string to iterate through its digits
  num_str = str(num)
  
  # Calculate the sum of factorials of digits
  digit_factorial_sum = sum(factorial(int(digit)) for digit in num_str)
  
  # Check if the sum is equal to the original number
  return digit_factorial_sum == num

def main():
  
  # Prompt the user to enter a number
  num = int(input("Enter a number: "))
  
  # Check if the number is a strong number
  if is_strong_number(num):
      print(num, "is a strong number.")
  
  else:
      print(num, "is not a strong number.")


main()