# 6.2 LIST OPERATIONS
print("6.2 LIST OPERATIONS")

# Concatenation
words = ["hello", "world", "test"]
release = ["alpha", "beta", "gamma"]
extended = words + release
print(extended)

# Multiplication
print(words*3)
print(words*4)

# Selecting a Subsequence in the list - Slicing
new_ver = words
print(new_ver)
print(new_ver[1:])
print(new_ver[:2])
print(new_ver[::2])


# 6.3 EDITING A LIST
print("\n\n6.3 EDITING A LIST")
new_ver[0] = "goodbye"
print(new_ver)

# 6.4 LISTS OF LISTS
print("\n\n6.4 LISTS OF LISTS")
name_result = [["Jake", 9], ["Finn", 6], ["Oliver", 9], ["Alex", 7]]
print(name_result)
print(name_result[0][0]) # prints the first element in the first list of lists
print(name_result[1][0]) # prints the first element in the second list of lists


# ---------------- LIST METHODS ----------------

"""append()"""
name_result.append(["Matt", 4])
print(name_result)

"""insert()"""
name_result.insert(1, ["kniip", 9])

"""sort()"""
name_result.sort()
print(name_result)

"""count()"""
y = [2, 10, 15, 23, 30, 35, 38, 2]
print(y.count(2)) # returns number of occurences of a given element

"""extend()"""
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(x)
x.extend(y) # adds an iterable (y) to the end of x.
print(x)

"""pop()"""
seven_multiples = [7, 14, 21, 28, 35, 42]
print(seven_multiples)
seven_multiples.pop() # pops the last element in the list
print(seven_multiples)

"""remove()"""
seven_multiples.remove(7) # removes the first occurence of this element, if any
print(seven_multiples)

"""reverse()"""
seven_multiples.reverse() # reverses every element 
print(seven_multiples)

"""index()"""
dupe = [8, 5, 12, 9]
print(dupe.index(12)) # finds the index of the first occurence of an element specified



# ---------------- MORE LIST METHODS ----------------
print("\n\n6.6 MORE LIST METHODS")

"""len()"""
coms = ['Lee', 'Adam', 'Peter', 'Clive']
print(len(coms)) # returns the length of the entire list (i.e. 4)


"""in operator (this is a statement operator, not a method)"""
print('Lee' in coms) # this stmt is used to test if 'Lee' is in the list named coms

"""min() and max()"""
xx = ["Kev", "Ip", "Sven"]
yy = [5, 6, 7]
print(min(yy)) # returns the minimum valued element (numbers sorted by their size)
print(min(xx)) # returns the minimum valued element (letters sorted alphabetically)

print(max(yy)) # returns the maximum valued element (numbers sorted by their size)
print(max(xx)) # returns the maximum valued element (letters sorted alphabetically)
