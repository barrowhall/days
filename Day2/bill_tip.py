print('welcome to the tip calculator')

bill = float(input('What was to total bill? $'))
tip = int(input('How much tip percentage would you like to give? 10, 12 or 15? '))
people = int(input('How many people will split the bill ? '))

tip_cal = round(tip / 100 * bill, 2)
calc = tip / 100 * bill + bill

indiv = calc / people

print(f'This is the tip {tip_cal}')

print(f'This is the bill including the tip {calc}')

print(f'This is the share including the tip {indiv}')


# All the calculations in one line

fina = (tip / 100 * bill + bill) / people

# Formating to show 2 decimals
fina = "{:.2f}".format(fina)


print(f"Each person should pay :  ${fina} ")