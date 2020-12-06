# storing file path and opening file
file_path = input('Please enter your file path: ')
wet_file = open(file_path, 'r')

# saving lines
lines = wet_file.readlines()
