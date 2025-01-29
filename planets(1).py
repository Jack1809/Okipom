### filename.py
### COMSC 175, Student Name
### Month Day, Year
### Time Spent = 



planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

with open('planets.txt', 'w') as planets_file:
    for planet in planets:
        planets_file.write(f"{planet}\n")

plst = []

with open('planets.txt', 'r') as planets_file:
    for line in planets_file:
        capitalized_planet = line.strip().capitalize()
        plst.append(capitalized_planet)

print(plst)

