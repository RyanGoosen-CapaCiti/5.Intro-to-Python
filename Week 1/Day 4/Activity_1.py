from math import floor
water = float(input('Enter number of liters: \n'))
bottles = floor(water/0.5)
remainder = round((water - (bottles * 0.5)),2)

print(f'{round(water,2)} water will fill {int(bottles)} bottles({remainder}L remains)')