
# Dictionary containing note_id:note_value
# These are swiped when the program exits
user_notes = {}

def output_all_notes():
  """Output all notes, starting at index 0."""
  print("Your notes:\n\n")

  # Condition that checks if there are no notes
  if not user_notes:
    print("None!")

  # enumerate assigns an index to each iteration
  # which is faster than incrementing a counter
  for i, note in enumerate(user_notes.values()):
    print(f"{i}. {note}")


def change_note_by():
  """Change the value of a note by its number."""

  # Loop 10 times
  for i in range(10):

    # Set the key of dictionary as the index and the value as the input
    user_notes[i] = input("Enter the value of your new note: ")
    print("\n")


# Main program - calling functions

change_note_by()
output_all_notes()