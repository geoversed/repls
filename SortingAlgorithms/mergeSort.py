def merge(left, right):
  merged = []
  left_index = 0
  right_index = 0

  # Merge the two arrays in sorted order
  while left_index < len(left) and right_index < len(right):
      if left[left_index] < right[right_index]:
          merged.append(left[left_index])
          left_index += 1
      else:
          merged.append(right[right_index])
          right_index += 1

  # Add the remaining elements from the left and right arrays
  merged += left[left_index:]
  merged += right[right_index:]

  return merged

def start(arr):
  """
  Sorts an array using the Merge Sort algorithm.

  Args:
  arr: List of elements to be sorted

  Returns:
  Sorted list in ascending order
  """

  if len(arr) <= 1:
      return arr

  # Split the array into two halves
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursive calls to merge_sort for both halves
  left_half = start(left_half)
  right_half = start(right_half)

  # Merge the sorted halves
  return merge(left_half, right_half)