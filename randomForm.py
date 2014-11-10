answer = "*** "

print "What is your name?"
name = raw_input(answer)
print "What do you want to be called?"
nick_name = raw_input(answer)

print "Your name is %r but you want to be called by %r" % (
	name, nick_name)