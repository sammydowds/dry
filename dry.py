# function to update a dictionary of each set of characters
def add_chars(dryness_dict, entry, line_num):
    if dryness_dict.has_key(entry):
        dryness_dict[entry][0] += 1
        dryness_dict[entry][1].append(line_num)
    else:
        dryness_dict[entry] = [1, [line_num]]
    return dryness_dict


# storing file path and opening file
file_path = input('Please enter your file path: ')
wet_file = open(file_path, 'r')

# saving lines
lines = wet_file.readlines()

# creating dict with words/characters and line numbers
dry_dict = {}
for line in range(len(lines)):
    char_entry = ''
    for char in lines[line]:
        if char != ' ':
            char_entry = char_entry + char
        elif char_entry != '' and not char_entry.isspace() and not len(char_entry) == 1:
            dry_dict = add_chars(dry_dict, char_entry, line)
            char_entry = ''


# sorting and presenting top repeats
sorted_dict = sorted(dry_dict.items(), key=lambda x: x[1][0], reverse=True)
for i in range(len(sorted_dict[0:6])):
    rep_str = str(sorted_dict[i][1][0])
    value_str = str(sorted_dict[i][0])
    print(str(i) + '. ---> ' + value_str + ' seen ' +
          rep_str + ' times in this file.')
