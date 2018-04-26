#------------------------------------------------------------
#Quiz: Booleans, Comparison Operators, and Logical Operators
#------------------------------------------------------------
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
if(san_francisco_pop_density>rio_de_janeiro_pop_density):
    print(True)
else:
    print(False)
#-- their method
print(san_francisco_pop_density > rio_de_janeiro_pop_density)

#------------------------------------------------------------
#Quiz: Conditional Statements
#------------------------------------------------------------

points = 174  # use this input when submitting your answer

# write your if statement here
result = ""

if(points>=1 and points<=50):
    result = "Congratulations! You won a wooden rabbit!"
elif(points>=51 and points<=150):
    result = "Oh dear, no prize this time."
elif(points>=151 and points<=180):
    result = "Congratulations! You won a wafer-thin mint!"
elif(points>=181 and points<=200):
    result = "Congratulations! You won a penguin!"
else:
    result = "Oh dear, no prize this time."

print(result)

#------------------------------------------------------------
#More Conditional Quizzes
#------------------------------------------------------------
# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "MN"
purchase_amount = 100

if (state is "CA"):
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif (state is "MN"):
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif (state is "NY"):
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

#--------------------------------------------------------------------------
#Quiz: Boolean Expressions for Conditions - truth value of the variable
#--------------------------------------------------------------------------
points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize is None
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)

#--------------------------------------------------------------------------
#Quiz: For Loops
#--------------------------------------------------------------------------
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ","_"))

print(usernames)

#-- using range for the list modification operation, get the values in the range and pass in the range variable into List index and manipulate the values in the
    #--in the list itself
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i]=usernames[i].lower().replace(" ","_")

print(usernames)
    #--to print the username List

#----------------------------------------------------------------
# Quiz: Create an HTML List
#----------------------------------------------------------------
Write a for loop that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
lengthoflist =len(items)
html_str = "<ul>"
# write your for loop here
for each in range(len(items)):
    html_str += "\n<li>"+items[each]+"</li>"

html_str +="\n</ul>"
print(html_str)

#####BETTER SOLUTION
items = ['first string', 'second string']

html_str = "<ul>\n"
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)


#----------------------------------------------------------------
# Quiz: While Loops---> Quiz: Nearest Square
#----------------------------------------------------------------
limit = 40
nearest_square = 0
i = 1
# write your while loop here
while (i*i) < limit:
    nearest_square = i*i
    i +=1

print(nearest_square)
