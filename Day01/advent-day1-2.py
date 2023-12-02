# filepath = 'inputs.txt'
filepath = 'puzzle-input.txt'

def read_file_lines():
    file1 = open(filepath, 'r')
    Lines = file1.readlines()
    return map(lambda x:x.strip(), Lines) # Strips the newline character


def convert_line_to_digits(input_line):
    digits_as_letters = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    final_digits_list = []

    counter = 0
    for char in input_line:
        if char.isdigit():
            final_digits_list.append(char)
        else:
            for digit in digits_as_letters:
                if input_line[counter:].startswith(digit):
                    final_digits_list.append(digits_as_letters[digit])

        counter += 1


    return final_digits_list

def main():

    Lines_no_new_line = read_file_lines()

    final_sum = 0
    for line in Lines_no_new_line:
        line_as_digits = convert_line_to_digits(line)
        cat_nums_list = line_as_digits[:1] + line_as_digits[-1:]
        cat_nums_joined = int("".join(cat_nums_list))
        final_sum += cat_nums_joined

    print(final_sum)

if __name__ == "__main__":
    main()
