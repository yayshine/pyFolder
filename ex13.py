from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

random = raw_input("So, what's up? ")
print "I'm a parrot, %r" % random