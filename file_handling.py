import os

'''
Open function
-------------
The access modes available for the open() function are as follows:

r: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
rb: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
w: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
wb: Opens a write-only file in binary mode.
w+: Opens a file for writing and reading.
wb+: Opens a file for writing and reading in binary mode.
a: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
ab: Opens a file for appending in binary mode.
a+: Opens a file for both appending and reading.
ab+: Opens a file for both appending and reading in binary mode.
'''
open_file = open("file_operations.txt", "r")

# Write and ovverride the file
# for i in range(0,6):
# 	open_file.write("\n Line")

# Rename file
# os.rename('file_operations.txt', 'file_operation.txt')

# Remove file
# os.remove('file_operations.txt')

# Return the name of the file
# open_file.name

# Check mode used while opening file
# open_file.mode

# seek function sets the reading star position in the file
# open_file.seek(13)

# tell function shows the position of pointer in a number
# print(open_file.tell())

# .readline funtion returns the file line of file, can also return number of string by passing number in parameter
# print(open_file.readline())

# .readlines() reads all of the text and split them into lines
# print(open_file.readlines())

for lines in open_file:
	print(lines)

# Close opened file
# open_file.close()
