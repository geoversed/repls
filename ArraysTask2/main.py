# Arrays and Lists
# Function to output the contents of a list

def OutputList(sentence):

    for Word in sentence:
      print(Word + " ", end="")

# Main program
sample_sentence = ["The", "quick", "brown", "fox", "jumps"]
OutputList(sample_sentence)

print("\n")  # newline to notice the difference

# Modify elements of that list
sample_sentence[1] = "small"
sample_sentence[2] = "grey"
sample_sentence[3] = "squirrel"
OutputList(sample_sentence)