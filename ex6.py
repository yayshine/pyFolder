# x has a formatter %d which is replaced by 10
x = "There are %d types of people." % 10
# binary stores the string "binary"
binary = "binary"
# do_not stores the string "don't"
do_not = "don't"
# y has two formatters, the variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x and y
print x
print y

# %r replaces string in ''
print "I said: %r." % x
# %s replaces string
print "I also said: '%s'." % y

# hilarious stores Boolean value False
hilarious = False
# joke_evaluation stores a string with formatter in it
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evalution while hilarious is the value to replace the formatter
print joke_evaluation % hilarious

# strings
w = "This is the left side of..."
e = "a string with a right side."

# strings are combined
print w + e