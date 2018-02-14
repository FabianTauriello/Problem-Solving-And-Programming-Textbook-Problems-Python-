# This program writes three lines of data to a file

# Open a file named name.txt
file_variable = open('name.txt', 'w')

# Write the names of three philosophers to the file
file_variable.write('John Locke\n')
file_variable.write('David Hume\n')
file_variable.write('Edmund Burke\n')

# Close the file
file_variable.close()
