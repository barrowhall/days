print('Leap Year Checker !!!')

year = int(input('What year do you want to check? '))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print('It is a leap year (400)')
		else:
			print('Is not a leap year(400)')
	else:
		print('Is  a leap year(100)')
else:
	print('Is not a leap year (4)')