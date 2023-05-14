# Activity 1: This activity will be an individual activity and will be graded.
# Time: 30 minutes
# Instructions
# Write a program that removes all numbers (except 5) that appear in a string.
# Output:
# >>>
# Enter a string that contains numbers: JGDN8923487854t6fnjhasfu555335udvb
# New string:
# JGDN5tfnjhasfu5555udvb
# >>> 

string = 'JGDN8923487854t6fnjhasfu555335udvb'
new_string = ''
for i in string:
    if type(i).isdigit(i):
        if i != '5':
            pass
        else:
            new_string += i
    else:
        new_string += i

print(new_string)