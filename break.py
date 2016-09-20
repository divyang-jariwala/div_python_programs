# program for simple demostration  of break statement
# program name : break.py

while True:
	s = raw_input('Enter something : ') # to take a input from user
	if s == 'quit':
		break # its will break the execution of program
	print 'Length of the string is', len(s)
print 'Done'
