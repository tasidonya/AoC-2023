import re
import multiprocessing.dummy as mp

filepath = 'inputs.txt'
# filepath = 'puzzle-input.txt'

all_lines = []
states = []

def is_char_a_symbol(input_char):
	if input_char in '#/*-+&$=@%':
		return True
	else:
		return False

def populate_states():
	# I am basing this off the assumption that all elements are the same size
	# y length = len(all_lines[0])
	# x length = len(all_lines)

	for x, line in enumerate(states):
		for original_line in all_lines:
			for y, char in enumerate(original_line):
				print(y, " ", char,  " ", x, " ", line, " ", original_line)
				states[x][y][char] = is_char_a_symbol(char)

def main():
	for line in open(filepath,'r').read().split('\n'):
		all_lines.append(line)

	states = [[{}] * len(all_lines[0])] * 10
	p = mp.Pool(4)
	p.map(populate_states)

	print(states)


if __name__ == "__main__":
    main()
