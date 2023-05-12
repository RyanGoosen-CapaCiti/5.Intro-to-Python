menu = {
    1:  ['CiTi burger',22.00],
    2:  ['CiTi pie',12.00],
    3:  ['Sausage/Russian roll',13.00],
    4:  ['Russian roll and chips',20.00],
    5:  ['Small chips',10.00],
    6:  ['Big chips',20.00],
    7:  ['Coke (350ml)',9.00]
}
display = '''
1.  CiTi burger             R22.00
2.  CiTi pie                R12.00
3.  Sausage/Russian roll    R13.00
4.  Russian roll and chips  R20.00
5.  Small chips             R10.00
6.  Big chips               R20.00
7.  Coke (350ml)            R9.00
'''
display = display.replace('.', ':')
print(f'This is our menu: {display}')

option = int(input('What would you like to order?: '))

if option not in menu.keys():
    print('Sorry, you’ve entered an invalid number!')
else:
    print(f'{menu[option][0]} costs R{menu[option][1]}')