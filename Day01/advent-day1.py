import re 

file1 = open('puzzle-input.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
Lines_no_new_line = map(lambda x:x.strip(), Lines)

sum = 0
separator = ''
for line in Lines_no_new_line:
	matches = re.findall("\d", line)
	first_and_last = (matches[0], matches[len(matches)-1])
	parsed_cat_matches = int(separator.join(first_and_last))
	sum += parsed_cat_matches

print(sum)
