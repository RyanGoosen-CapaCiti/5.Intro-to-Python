# Activity 2: This activity will be an individual activity and will be graded.
# Time: 60 minutes
# Instructions
# Write a program that prompts a user to enter a cell phone number in a certain format: +2778-123-4567
# The number must start with "+27" (standard South-African number). A message must be printed indicating if the number is in the correct format.
# An error message must be printed if the wrong country code is entered or the number is in an incorrect format.
# Output:
# >>>
# Enter a number: +2745-789-4578
# The number is in the correct format
# >>> ============== RESTART ==================
# >>>
# Enter a number: +2745-7849-457
# The number is in the incorrect format
# >>>=============== RESTART ==================
# >>>
# Enter a number: 
# The number is in the incorrect format
# >>> 69 10

number = '+2745-789-45578'
if len(number) != 14:
    print('Number length incorrect')
elif number[:3] != '+27':
    print('Wrong format')
elif type(number[3:5]).isdigit(number[3:5]) == False or type(number[6:9]).isdigit(number[6:9]) == False or type(number[10:]).isdigit(number[10:]) == False :
    print('Wrong format')
