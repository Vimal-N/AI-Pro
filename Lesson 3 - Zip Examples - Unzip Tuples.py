#Unzip the cast tuple into two names and heights tuples.


cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = {} #initializing tuple
heights ={} #initializing tuple

#unzip command syntax
names,heights = zip(*cast)

#printing the tuples below
print(names)
print(heights)
