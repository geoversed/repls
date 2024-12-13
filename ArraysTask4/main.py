# Arrays and Lists

# this is a list comprehension
# rather than appending to the list, elements needed are 
# already added as soon as it is defined
Product = [["" for X in range(2)] for Y in range(4)]


# Subroutine to put data into the list
def NewDatabase():

    # This stmt ensures changes in the enclosing scope
    # affect the global scope as well
    global Product
    Product[0][0] = "Cornflakes" ; Product[0][1] = "1.40"
    Product[1][0] = "Weetabix" ; Product[1][1] = "1.20"


# Subroutine to output a product from the list
def OutputProduct(Number):

  # ensures we access the correct data
  global Product
  print("{}: £{}".format(Product[Number][0], Product[Number][1]))


# Main program
NewDatabase()
OutputProduct(1)