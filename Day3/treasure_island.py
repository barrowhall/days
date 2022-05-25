print('Welcome to Treasure Island !!!!')
print('Your mission is to find the treasure')

one = input('You are at a road crossing. Where do you want to go ? Type "left" or "right" ')

if one == 'left':
	doi = input('You have reached a river. What do you want to do ? Type "swim" or "wait" ')
	if doi == 'wait':
		print('A boat came an took you to the other side of the river.')
		trei = input('You walkedto a castle and in the court are three coloured doors. Type "blue" , "red" or "yellow" ')
		if trei == 'blue':
			print('You entered the treasure room. You Win !!!!!')
		elif trei == 'yellow':
			print('You entered a room full of angry Dragons. GameOver !!!!')
		elif trei == 'red':
			print('You entered a room full of lava. GameOver !!!!')
		else:
			print('This is not a coloured door')
	
	elif doi == 'swim':
		print('A crocodile came and ate you. GameOver!!!!')
	
elif one == 'right':
	print('A train came from right and hit you. GameOver!!!!')

else:
	print('This is not an answer')
