print('Welcome to Pizza Ordering')
price = 0


size = input('What size pizza do you want ? S, M or L ? ')
pepe = input('Do you want pepperoni? Y or N ? ')
ches = input('Do you want extra cheese ? Y or N ? ')


if size.upper() == 'S':
	price = 15
	if pepe.upper() == 'Y':
			price += 2
	if ches.upper() == 'Y':
			price += 1
	print(f'You want small pizza, and it will cost ${price}')
elif size.upper() == 'M':
	price = 20
	if pepe.upper() == 'Y':
		price += 3
	if ches.upper() == 'Y':
		price += 1
	print(f'You want medium pizza, and it will cost ${price}')
elif size.upper() == 'L':
	price = 25
	if pepe.upper() == 'Y':
		price += 3
	if ches.upper() == 'Y':
		price += 1
	print(f'You want large pizza, and it will cost ${price}')
else:
	print('This is not a size')
	
# Another way to do it

if size.upper() == 'S':
	price += 15
elif size.upper() == 'M':
	price += 20
elif size.upper() == 'L':
	price += 25
else:
	print('Not a pizza size .')
	
if pepe.upper() == 'Y':
	if size.upper() == 'S':
		price += 2
	elif size.upper() == 'M':
		price += 3
	elif size.upper() == 'L':
		price += 3
	else:
		print('Not an option')
if ches.upper() == 'Y':
	price += 1

print(f'The total price is {price} ')
	
