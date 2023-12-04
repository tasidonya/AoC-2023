import re
import numpy
# import copy

filepath = 'inputs.txt'
# filepath = 'puzzle-input.txt'


def main():
	all_lines = []
	for line in open(filepath,'r').read().split('\n'):
		all_lines.append(line)

	# I am basing this off the assumption that all elements are the same size
	# y length = len(all_lines[0])
	# x length = len(all_lines)

	a_line = [{"Blank":False} for i in range(len(all_lines[0]))]
	print(len(all_lines))
	all_lines_as_dict = [numpy.repeat([a_line], range(len(all_lines)))]

	print(all_lines_as_dict[0])

if __name__ == "__main__":
    main()
