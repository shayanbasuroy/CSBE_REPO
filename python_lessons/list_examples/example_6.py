students = [
    [
        {"name": "Alice", "age": 25, "grades": {"Math": 90, "English": 85}},
        {"name": "Bob", "age": 22, "grades": {"Math": 80, "English": 88}}
    ],
    [
        {"name": "Charlie", "age": 23, "grades": {"Math": 85, "English": 90}},
        {"name": "David", "age": 24, "grades": {"Math": 92, "English": 91}}
    ]
]
# Access Charlie's name
charlie_name = students[1][0]["name"]
print(charlie_name)  # Output: Charlie

# Access Bob's age
bob_age = students[0][1]["age"]
print(bob_age)  # Output: 22

# Access Alice's Math grade
alice_math_grade = students[0][0]["grades"]["Math"]
print(alice_math_grade)  # Output: 90


# Update David's age
students[1][1]["age"] = 25
print(students[1][1]["age"])  # Output: 25
