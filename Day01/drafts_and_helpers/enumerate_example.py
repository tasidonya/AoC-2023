lists_of_numbers = [[1,2,3], [4,5,6], [7,8,9]]
for index, nested_list in enumerate(lists_of_numbers):
        print("Outside " + str(index) + " " + str(nested_list))
        for second_index, element in enumerate(nested_list):
            print(second_index, element)