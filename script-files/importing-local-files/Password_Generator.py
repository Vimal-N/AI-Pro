#Write a function called generate_password that selects
#three random words from the list of words word_list
#and concatenates them into a single string.
#Your function should not accept any arguments and
## should reference the global variable word_list to build the password.
# Use an import statement at the top

###########################################################
############ password_generator.py
import random
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)
#print(word_list)

# Add your function generate_password here
def generate_password():
    password = ""
    #print(random.choice(word_list))
    for i in range(3):
        random_word = random.choice(word_list)
        #print(random_word)
        password +=random_word
        #password = password + (random.choice(word_list))
    return password
# It should return a string consisting of three random words
# concatenated together without spaces



# test your function
print(generate_password())

########################################################################
################### word.txt from which the three words for pwd is taken
# Alice
# was
# beginning
# to
# get
# very
# tired
# of
# sitting
# by
# her
# sister
# bank
# having
# nothing
# Once
# twice
# she
# had
# peeped
# into
# the
# book
# her
# sister
# was
# reading
# but
# it
# had
# no
# pictures
# or
# conversations
# in
# it
# and
# what
# is
# the
# use
# of
# a
# book
# thought
# Alice
# without
# pictures
# or
# conversations


### their answer
#Quiz Solution: Password Generator
#To create random passwords we used import random. The function definition was simply:

#def generate_password():
#    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

#Alternatively, you could use the random.sample function and .join method for strings:

#def generate_password():
#    return ''.join(random.sample(word_list,3))
