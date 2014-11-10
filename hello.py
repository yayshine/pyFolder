#!/usr/bin/python2.6 -tt
# Copyright 2014 Yayshine All Rights Reserved.

# Using the external module sys
import sys

# Define a main() function that prints a little greeting.
def main():
	print "Hai"
	print sys.argv

# This is the standard boilerplate that calls the main() function.
# This is true only when the file is "run" by the interpreter
if __name__ == '__main__':
	main()