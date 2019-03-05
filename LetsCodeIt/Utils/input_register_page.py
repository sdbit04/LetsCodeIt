import csv
import os
relative_input_file = "..\\Input_data\\input2register"
current_dir = os.path.dirname(__file__)
input_file = os.path.realpath(os.path.join(current_dir, relative_input_file))
print(input_file)


def get_data():
    data_list = []
    with open(input_file, 'r') as in_file:
        csv_file = csv.reader(in_file)
        # csv_file is a generator type iterator, we get a list on execution of every next()
        print(csv_file)
        # next line is to avoid header line from the for loop below
        print(next(csv_file))
        ####################### Experimental block ###############################
        csv_file_dict = csv.DictReader(in_file)
        # csv_file_dict is a generator type iterator, we get a ordered dict on execution of every next()
        print(csv_file_dict)
        print(next(csv_file_dict))
        print(next(csv_file_dict))
        dict1 = next(csv_file_dict)
        print(dict1)
        print(dict1['EMAIL'])
        #######################################################################
        for line in csv_file:
            data_list.append(line)
        return data_list


list1 = get_data()
# for line in list1:
#     print(line)

# print(list1)
