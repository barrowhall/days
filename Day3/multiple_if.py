print("Welcome to the rollercoaster .")

height = int(input('What is your height? '))
bill = 0

if height > 120:
	print("You can ride the rollercoaster!")
	age = int(input('What is your age? '))
	if age < 12:
		bill = 5
		print('The ticket cost is  $5')
	elif age <= 18:
		bill = 7
		print('The ticket cost is  $7')
	else:
		bill = 12
		print('The ticket cost is  $12')
		
	photo = input('Do you want a photo? Answer with Y / N : ')
	
	if photo.upper() == 'Y':
		bill += 3
	print(f'The total cost is ${bill}')
else:
	print('Sorry, you have to grow taler to ride de rollercoaster :(')
