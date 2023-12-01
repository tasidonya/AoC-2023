import re 

filepath = 'inputs.txt'
# filepath = 'puzzle-input.txt'

def read_file_lines():
    file1 = open(filepath, 'r')
    Lines = file1.readlines()
    return map(lambda x:x.strip(), Lines) # Strips the newline character

def fused_number_check(input_str):
    is_fused = False
    fusion_value = ""
    fused_list = {'oneight': (1, 8), 'threeight': (3, 8), 'fiveight': (5, 8), 'nineight': (9, 8)}

    for item in fused_list:
        if item in input_str:
            is_fused = True
            fusion_value = fused_list[item]

    return (is_fused, fusion_value)

def convert_line_to_digits(input_line):
    digits_as_letters = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}


    if (input_line == "oneight"):
        return [1, 8]

    built_string = ""
    final_digits_list = []
    for char in input_line:
        if char.isdigit():
            final_digits_list.append(int(char))
        else:
            built_string += char
            print(built_string)
            fused_number = fused_number_check(built_string)
            if fused_number[0]:
                final_digits_list.append(fused_number[1])
                built_string = ""
            elif built_string in digits_as_letters:
                final_digits_list.append(digits_as_letters[built_string])
                built_string = ""
    if len(built_string) > 4:
        for char in built_string:
            

    return final_digits_list
            

def main():

    Lines_no_new_line = read_file_lines()

    for line in Lines_no_new_line:
        print(line)
        line_as_digits = convert_line_to_digits(line)
        print(line_as_digits)


if __name__ == "__main__":
    main()
