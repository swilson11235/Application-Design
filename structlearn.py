import struct
import sys
# four_bytes = b_file.read

# results =struct.unpack("<i", four_bytes)


# ###pack your information

# your_int = 42

# bytes = struct.pack("<i", your_int)

filename = sys.argv[1]
my_file = open(filename, 'r')
my_bytes = my_file.read(22)

num_channels =srtuc.unpack("<i", my_file.read(2)
print num_channels
