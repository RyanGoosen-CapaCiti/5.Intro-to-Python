# file_name = finance_calculators.py
# Input should not be case sernsitive
# Investment steps?
#   Inputs:
#       interest rate = 8 != 8%
        # years investing for
        # simple or compound rates
        # simple  A = P(1 + r * t) 
        # compound  A = P(1 + r) ^ t
            # ●     ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
            # ●     ‘P’ is the amount that the user deposits.
            # ●     ‘t’ is the number of years that the money is being invsted for.
            # ●     ‘A’ is the total amount once the interest has been applied.
# Bond steps ?
    # Inputs
        # ●     The present value of the house. E.g. 100000
        # ●     The interest rate. E.g. 7
        # ●     The number of months they plan to take to repay the bond. E.g. 120
        # formula
            # repayment = x = (i.P)/(1 - (1+i)^(-n))
            #  ●     ‘P’ is the present value of the house.
            #  ●     ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
            #  ●     ‘n’ is the number of months over which the bond will be repaid.

def investment():
    r = input('Interest')
    p = input('Amount')
    t = input('Years')
    f = input('Compound or Simple')
    if f == compound:
        A = p(1 + r) ^ t
    else:
        A = p(1 + r * t)

def bond():
    p = input('Value')
    i = input('Intereset')
    n = input('Month')
    x = (i.p)/(1 - (1+i)^(-n))

choice = input('Bond or investmewnt: ')
if choice == 'bond':
    bond()
elif choice == 'investment':
    investment()