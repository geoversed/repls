# Arrays and Lists
# Function to output the contents of a list

def OutputList(sentence: list[str]) -> None:
  
  for Word in sentence:
    # end kwarg ensures no newlines are created when looping over
    # the current sentence
    print(Word + " ", end="")
  print()  # newline only once loop is done


"""Main program"""
sample_sentence = []

# _ is used to tell python we will not use the loop counter
for _ in range(2):
  sample_sentence.append("")  # for testing

# override original contents
sample_sentence[0] = "Hello"
sample_sentence[1] = "World"

# Call the function
OutputList(sample_sentence)