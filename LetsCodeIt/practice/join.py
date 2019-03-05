my_list = ["a", "b", "c", "d"]
print(my_list)
# Want to convert this into string;
my_string = ''
for i in my_list:
    my_string += i # This steps creates an object  each time, as string in immutable

print(my_string)

print("So the best is to use join")
join_string = ''
join_string = join_string.join(my_list)
print(join_string)

for i in join_string:
    print("{},".format(i), end='')

print()
print(",".join(join_string))

