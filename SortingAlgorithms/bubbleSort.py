def start(arr: list):
  """
  Sorts an array using the Bubble Sort algorithm.

  # Parameters
  arr: List of elements to be sorted

  # Returns
  Sorted list in ascending order
  """

  n = len(arr)

  # Traverse through all array elements
  for i in range(n):

      # Flag to check if any swapping is done in this pass
      swapped = False

      # Last i elements are already in place
      for j in range(0, n-i-1):

          # Swap if the element found is greater
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
              swapped = True

      # If no two elements were swapped, array is already sorted
      if not swapped:
          break
  return arr