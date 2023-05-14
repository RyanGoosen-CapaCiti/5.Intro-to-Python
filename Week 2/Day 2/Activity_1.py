def convert(temp):
    temp = int(temp)
    celc = (5 / 9) * (temp - 32)
    return round(celc)


def highest(temp1, temp2):
    temp1 = convert(temp1)
    temp2 = convert(temp2)
    if temp1 > temp2:
        highest = temp1
    else:
        highest = temp2
    return highest

tempratures = input('Max temp fpr the past 2 days: ')
temp = tempratures.split(' ')
print(highest(temp[0], temp[1]))