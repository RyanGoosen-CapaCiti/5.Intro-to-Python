def part1():
    count = 1
    for i in range(1,4):
        if i == 2 or i == 3:
            count += 3
            print('\n')
        print(count , count + 1 , count + 2)
    
def part2():
    number = int(input('Please enter the number: '))
    sedan = 0
    luxuary = 0
    commericial = 0
    
    while number != 0:
        #1 = luxury, 2 = commercial, 3 = sedan
        if number == 1:
            luxuary += 1
        elif number == 2:
            commericial += 1
        elif number == 3:
            sedan += 1
        else:
            number = int(input('Please enter the number: '))
        number = int(input('Please enter the number: '))
    print(f"There where a total of {sedan+luxuary+commericial} cars: comprising of {luxuary} luxuary cars, {commericial} commericial cars, {sedan} sedan cars")

def part3():
    count = 1
    while True:
        if count == 5:
            break
        else:
            print('Not yet', count)
        count += 1

part3()