#Use a list comprehension to create a new list first_names
#containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
#for name in names:
    #name.split()[0].islower
 #   print(name.split()[0].lower())
print(first_names)
