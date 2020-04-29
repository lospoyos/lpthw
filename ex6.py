# Types of people in binary :3
types_of_people = 10
# String with the amount of types of people inside of it
x = f"There are {types_of_people} types of people."

# Just a place to store the string binary
binary = "binary"
# Do not string
do_not = "don't"
# String with the explanation of the joke
y = f"Those who know {binary} and those who {do_not}."

# Print the first sentence stored in x
print(x)
# Print the second sentence stored in y
print(y)

# Print it again, but used as a quote and the f string format
print(f"I said: {x}")
# Them same but for the second sentence
print(f"I also said: '{y}'")

# Save the boolean false into hilarious
hilarious = False
# Create a string with an empty argument
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the string and add hilarious as an argument for joke_evaluation
print(joke_evaluation.format(hilarious))

# Another string with a sentence
w = "This is the left side of..."
# A fourth string with a sentence
e = "a string with a right side."

# Print both strings one after the other
print(w + e)
