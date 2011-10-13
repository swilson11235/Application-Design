
#####################################
## Stephen Wilson                  ##
## 10/04/11                        ##
## Application Design              ##
## Updated Statistical Calculator  ##
#####################################

This program can read and write a set of numbers from a text file to be analysed statistically. The numbers to be analysed need to be in the first line of the .dat file. Numbers can be manually entered as well.


Manual Input:
Typical input for the manual input of numbers is: Stephen 1 2 3 4 5 6. The one exception to this is the addition of numbers to a list that was loaded from file. In this case,the input would not include the name.

Saving the data:
All data will be saved in data.dat, regardless of if the file exists or if there was information in it previously.
If the saving of the numbers crashes, the data will be saved in a temp.dat file so as to prevent overwriting any desired data.

The text file output will resemble this:
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
[1.0, 6.0, 3.5, 1.707825127659933]

The first line is the inputed numbers, and the second line is the statistics: min, max, avg, stdev (respectively).

