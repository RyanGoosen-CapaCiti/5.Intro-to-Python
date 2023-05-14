# Failed = >60
# No distinction 60 < 80
# Distinction 80 <

mark = 0
count = 0

while True:
    number = int(input('Enter student mark: '))
    if number == 0:
        average = mark/count
        if average < 60:
            verdict = 'Fail'
        elif average < 80:
            verdict = 'Pass with no distinction'
        else:
            verdict = 'Pass with a distinction' 
        break
    else:
        mark += number
    count += 1

print(f'The student average is {average}, verdict: {verdict}')