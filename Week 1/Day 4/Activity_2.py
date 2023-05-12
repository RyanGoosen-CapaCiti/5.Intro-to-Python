dam_capacity = 1000000
water_released = int(input('How many milliliters of water were released? '))

print('================REPORT================')
print(f'Amount of water released {water_released/1000}L')
print(f'Amount of water left {dam_capacity - (water_released/1000)}')
print(f'Percentage: {(round((dam_capacity - (water_released/1000))/dam_capacity,2))*100}L')
print('================REPORT================')