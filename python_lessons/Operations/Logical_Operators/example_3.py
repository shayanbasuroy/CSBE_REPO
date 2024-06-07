"""
The not operator in Python is a logical operator used to combine two conditions. It returns True if both conditions are true, and False if at least one of the conditions is false.

"""
# Define some variables
age = 20
has_license = True

# Check if a person is eligible to drive
if not age >= 18 and has_license:
    print("The person is eligible to drive")
else:
    print("The person is not eligible to drive")

# Another example with different conditions
is_student = True
has_paid_fees = False

# Check if a student is allowed to attend classes
if not is_student and has_paid_fees:
    print("The student is allowed to attend classes")
else:
    print("The student is not allowed to attend classes")



"""
First Condition (age and has_license):

age is 20 and has_license is True.
The condition age >= 18 and has_license checks if the person is 18 or older and has a driving license.
Since both conditions are true (20 is greater than 18 and the person has a license), the result is True.
The code prints "The person is eligible to drive".
Second Condition (is_student and has_paid_fees):

is_student is True and has_paid_fees is False.
The condition is_student and has_paid_fees checks if the person is a student and has paid the fees.
Since one of the conditions is false (the fees have not been paid), the result is False.
The code prints "The student is not allowed to attend classes".
"""
