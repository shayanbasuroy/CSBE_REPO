#list.py

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

#
wizard_list = ['spider legs', 'toe of frog', 'eye of newt',
'bat wing', 'slug butter', 'snake dandruff']

print(wizard_list)

print(wizard_list[0])

wizard_list[2] = 'snail tongue'
print(wizard_list)

print(wizard_list[2:5])

wizard_list.append('bear burp')
print(wizard_list)

#Remove item
del wizard_list[5]
print(wizard_list)