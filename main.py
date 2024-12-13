# Arrays and Lists
# Function to output the contents of a list

# Create a function that takes in a sentence as a list of strings
def OutputList(sentence: list[str]) -> None:

    # Iterate through elements using enumerate func, start at 1
    # To avoid inaccurate index values, start kwarg is 1.
    for i, word in enumerate(sentence, start=1):
      print(f"Word {i} is {word}.")


# Main program
sample_sentence = ["The", "quick", "brown", "fox", "jumps"]
OutputList(sample_sentence)  # Call the function
