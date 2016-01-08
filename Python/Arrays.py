list_of_numbers = [0, 4, 2, 5, 1, 3]
list_of_strings = ["blackberry", "bilberry", "strawberry", "gooseberry", "blueberry"]
print(list_of_numbers)
print(list_of_strings)
list_of_numbers.sort()
list_of_strings.sort()
print(list_of_numbers)
print(list_of_strings)
list_of_numbers.append(6)
list_of_strings.insert(4, "tomato") #Adds tomato to fourth index of the string array
print(list_of_numbers)
print(list_of_strings)
#list_of_numbers.pop() #pops the last number of the array
list_of_numbers.pop(6) #pops number in the 6th index of array
list_of_strings.remove("tomato")

#Tuples - Lists that cannot change. Tuples create using '(' and ')' instead of '[' and ']'
screen_sizes = (800, 1280, 640, 460)

#Length can be accessed using len() function.
len("Tells how many characters")
len(["returns", "how", "many", "elements", "in", "array", "or", "tuple"])
len(screen_sizes)

#Iterating through array
# Where i is the counter, range is from 0 to (len(list_of_numbers)-1) inclusive
for i in range(0, len(list_of_numbers)):
    print(list_of_numbers[i]);

#Going thorough each element in the array.
for berry in list_of_strings:
    print(berry);
