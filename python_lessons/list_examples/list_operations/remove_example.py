"""
List Operations

append
clear
copy
count
pop



"""

fruits = ["apple", "banana", "cherry"]
# print(fruits)

# fruits.append("orange")
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

for fruit in fruits:
                    if fruit == 'banana':
                            print(fruit)
                            fruits.remove("banana")
print(fruits)

# fruits.remove("banana")
# print(fruits)  # Output: ['apple', 'cherry', 'orange']