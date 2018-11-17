import csv
input_file = r"C:\Users\dassw\PycharmProjects\LetsCodeIt\LetsCodeIt\Input_data\input2register"


def get_data():
    data_list = []
    with open(input_file, 'r') as in_file:
        csv_file = csv.reader(in_file)
        for line in csv_file:
            data_list.append(line)
        return data_list

#
list1 = get_data()
for line in list1:
    print(line)

