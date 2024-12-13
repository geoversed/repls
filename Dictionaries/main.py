a = {"name": "Mr G", "age": 16}

# Update the Dictionary
a.update({"age": 17})
a["age"] = 17

# Loop through Dictionary
for key, val in a.items():
 print(key, val)

# Loop through keys only
for key in a:
  print(key)

# Loop through values only
for val in a.values():
  print(val)

# Remove a key from the Dictionary
del a["age"]
a.pop("name")

# Clear the Dictionary
a.clear()
