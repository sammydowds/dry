# check if a line has already been accounted for
def check_vals(dict, val):
    for values in dict.values():
        if val in values:
            return False
    return True


# creat dict with number of first line as key, and repeat lines as values in an array
def compare(lines):
    split_a = lines
    split_b = lines
    dry_dict = {}
    for i in range(len(split_a)):
        if len(split_a[i]) > 3 and check_vals(dry_dict, i):
            for j in range(len(split_b)):
                if split_a[i] == split_b[j] and i != j:
                    if (i) not in dry_dict.keys():
                        dry_dict[i] = [j]
                    else:
                        dry_dict[i].append(j)
    return dry_dict


# filter repeat dict with parameters
def present_filter(dry_dict, lines, len_line=3, repeated=2):
    new_dict = {}
    sum_repeats = 0
    for key, value in dry_dict.items():
        if len(value) > repeated and len(lines[key]) > len_line:
            new_dict[key] = value
            sum_repeats = sum_repeats + len(value)
            print('-------------------------------------')
            print(lines[key], 'repeats on lines ', value)
    print(str(sum_repeats) + '/' + str(len(lines)), str(round(sum_repeats/(len(lines))*100)) + '%',
          'lines are duplicate lines |', 'with lines that occur more than:', repeated, 'times',
          '| and are longer than:', len_line, 'characters')


# storing file path and opening file
file_path = input('Please enter your file path: ')
wet_file = open(file_path, 'r')

# saving lines
lines = [line.strip() for line in wet_file]

# run
present_filter(compare(lines), lines, 8, 1)
