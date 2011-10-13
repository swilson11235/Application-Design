#############################
## Stephen Wilson          ##
## 10/03/11                ##
## Application Design      ##
## Statistical Calculator  ##
#############################

##############################################################################
## Functions:  Gathers input manually, and these numbers are analysed. This ##
## program can write a set of numbers to a text file that has been analysed ##
## statistically.                                                           ##
##############################################################################

#Import the math library for square root function
import math
end_ls = [] # Creates a new list for final output.
st_ls = [] # Declares a list to store statistics in
num_ls = [] # Creates a list for initial output.

#Gets input from user, splits the string into sub-strings
raw_ls = raw_input("\nEnter your name and then at least five numbers seperated by spaces: ")
num_ls = raw_ls.split()

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
# Or, if I'm allowed to, from the for loop can be replaced with:
#st_avg = math.fsum(end_ls) / len(end_ls)
st_ls.append(st_avg)

#Calculates stdev, and then appends them to the list
vari =0 
for n in end_ls:
	vari += (n - st_avg) ** 2
st_stdev = math.sqrt(vari / len (end_ls)) # calls the math library's square root function and calculates stdev
st_ls.append(st_stdev)

# Prints out the Statistics with the user's name. \n creates a new line, chr(39) is " ' ".
print "\n\nHere are the statistics for {name}'s list:\n".format(name = num_ls[0])
print 'Min is {0[0]}, Max is {0[1]}, Average is {0[2]}, and Standard deviation is {0[3]}\n'.format(st_ls)

#Opens a file and writes the stats and numbers if desired
prompt = raw_input("Save the file? (y or n): ")
if prompt=='y': # "Yes" condition
# Do you need me to say that I looked up general i/o in the python documentation http://docs.python.org/tutorial/?
	print 'Saving numbers and stats to data.dat\n'
	f = open("data.dat","w")
	f.write(str(end_ls))
	f.write("\n")
	f.write(str(st_ls))
	f.close()
elif prompt=='n': # "No" condition ### Looked up elif in python documentation
	print "Quitting..."
else: # Handles any other input
	f = open("error.dat","w")
	f.write(str(end_ls))
	f.write("\n")
	f.write(str(st_ls))
	f.close()
	raise ValueError, 'Error in input! Saving in error.dat...' # Raising ValueError found in python documentation
