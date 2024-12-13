# Import the random module
import random


# Function to generate a description of fictional animals that live on a planet
def generate_planet_description(planet_number):
    # Set the seed for the random number generator based on the planet number
    random.seed(planet_number)
    
    # Define lists of creatures, colors and characteristics
    creatures = ['lizards', 'humanoids', 'insects']
    colours = ['red', 'green', 'blue']
    characteristics = ['shy', 'angry', 'docile']
    
    # Randomly select a creature, color, and characteristic
    creature = random.choice(creatures)
    colour = random.choice(colours)
    characteristic = random.choice(characteristics)
    
    # Return the generated description
    return f"{characteristic} {colour} {creature}"

# Example usage
planet_number = 1650
description = generate_planet_description(planet_number)
print(description)