#############################
## Stephen Wilson          ##
## 10/03/11                ##
## Application Design      ##
## Statistical Calculator  ##
#############################

##################################################################################
## Functions: This program can read and write a set of numbers from a text      ##
## file to be analysed statistically. The numbers to be analysed need to be     ##
## in the first line of the .dat file. Numbers can be manually entered as well. ##
##################################################################################

#Import the math library for square root function
import math
end_ls = [] # Creates a new list for final output.
st_ls = [] # Declares a list to store statistics in
num_ls = [] # Creates a list for initial output.
filename = 'data.dat'
prompt = 'm'

prompt = raw_input("\nIf you want to get numbers for analysis from a file, enter f. \nIf you want to enter them manually, enter m.\n")

# The following if statement allows for the importing of a data file (default is data.dat) 
# or a manual entering of numbers for the calculator

# If getting numbers from a file, the user needs to have them in the first line of the text file
if prompt == 'f':
	user = raw_input("What is your name?\n")
	print "\n\nNOTE: Any numbers to be imported need to be in the first line of the .dat file. "
	filename = raw_input("Filename (default is data.dat): ")
	try:
		f = open(filename, "r")
	except IOError: # Deals with exceptions, such as if the file doesn't exist
		raise ValueError, 'Sorry, that filename does not exist. please reboot the program'
	raw_ls = f.readline() # The numbers are stored on the first line
	num_ls = (eval(raw_ls)) # Seperates the numbers in the string out into floats
	num_ls.insert(0,user)
	print 'This is your number set that was imported: '
	print num_ls
	prompt = raw_input('If you wish to add more numbers, enter y: ')
	if prompt == 'y':
		raw_ls = raw_input("Enter numbers one at a time seperated by spaces:")
		raw_ls = raw_ls.split() #Splits the string into component strings
		num_ls += raw_ls #Adds these strings to num_ls
	f.close()

elif prompt == 'm':
	#Gets input from user, splits the string into sub-strings
	raw_ls = raw_input("\nEnter your name and then at least five numbers seperated by spaces: ")
	num_ls = raw_ls.split()
else: # Handles any other input
	raise ValueError, 'Error in input! Try again later.'

#Takes input,converts it into floats, adds it to the output list, and sorts it.
for token in num_ls[1:]:
	end_ls.append(float(token))
	end_ls.sort()

#Calculates MIN and MAX, and then appends them to the stats list.
st_min = end_ls[0]
st_max = end_ls[len(end_ls)-1]
st_ls.append(st_min)
st_ls.append(st_max)

#Calculates avg, and then appends them to the list.
tot = 0
for i in end_ls:
	tot += i
st_avg = tot / len(end_ls)
# Or, if I'm allowed to:
#st_avg = math.fsum(end_ls) / len(end_ls)
st_ls.append(st_avg)

#Calculates stdev, and then appends them to the list
vari =0 
for n in end_ls:
	vari += (n - st_avg) ** 2
st_stdev = math.sqrt(vari / len (end_ls))
st_ls.append(st_stdev)

# Prints out the Statistics with the user's name. \n creates a new line, chr(39) is " ' ".
print "\n\nHere are the statistics for {name}'s list:\n".format(name = num_ls[0])
print 'Min is {0[0]}, Max is {0[1]}, Average is {0[2]}, and Standard deviation is {0[3]}\n'.format(st_ls)

#Opens a file and writes the stats to it if there are new numbers.
prompt = raw_input("Save the file? (y or n)")
if prompt=='y':
	print 'Saving numbers and stats to data.dat\n'
	f = open("data.dat","w")
	f.write(str(end_ls))
	f.write("\n")
	f.write(str(st_ls))
	f.close()
elif prompt=='n':
	print "Quitting..."
else: # Handles any other input
	f = open("temp.dat","w")
	f.write(str(end_ls))
	f.write("\n")
	f.write(str(st_ls))
	f.close()
	raise ValueError, 'Error in input! Saving in temp.dat...'
