# A program to calculate the length of a string.
var_string = "GROUP_FIVE_PROGRAMMING"
print(f"Length of the {var_string} is:")
print(f"Length: {len(var_string)}")
print()

#  A program counts the number of characters in a string.
var_string = "Hello_World!"
print(f"Number of characters {var_string} is:")
print(f"Number of characters: {len(var_string)}")
print()

# 💲 Replace repeated first character
our_word = "restart"
result = our_word[0] + our_word[1:].replace(our_word[0], '$')
print(result)
print()

# Swap first two characters of two strings
string_1 = "xxx"
string_2 = "yyy"

swap_string_1 = string_2[:2] + string_1[2:]
swap_string_2 = string_1[:2] + string_2[2:]

result = swap_string_1 + " " + swap_string_2
print(f"Original Strings: {string_1}, {string_2}")
print(f"Result: {result}")
print()

# Concatenate multiple variables
first_name = "Eliezar"
last_name = "Mingo"
age = "21"
grp = "Group_5"

full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Group: {grp}")
print()

# Concatenate user input
string1 = input("Enter the First Name: ")
string2 = input("Enter the Last Name: ")
result = string1 + " " + string2
print(f"Result: {result}")
print()

# Concatenate into a paragraph   
name = "Eliezar Mingo"
age = 21
paragraph = "My name is " + name + "\n and I am " + str(age) + " years old."
print(paragraph)
print()
