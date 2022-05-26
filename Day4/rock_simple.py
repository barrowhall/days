import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
lista = [rock, paper, scissors]
print("Let's play Rock-Paper-Scissors !!!!")

mas = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n '))


if mas >= 3 or mas < 0:
	print('Not a valid choice, You Lose :((')
	
else:

	aiur = random.randint(0, 2)
	comp = lista[aiur]
	tu = lista[mas]
	
	sign = ""
	signu = ""
	
	if aiur == 0:
		sign = 'Rock'
	elif aiur== 1:
		sign = 'Paper'
	elif aiur == 2:
		sign = 'Scissors'
		
	if mas == 0:
		signu = 'Rock'
	elif mas == 1:
		signu = 'Paper'
	elif mas == 2:
		signu = 'Scissors'	
		
		
	if mas == aiur:
		print(f'You choose {signu}.')
		print(tu)
		print(f'Computer chose {sign}.')
		print(comp)
		print('It is a tie ===')
	
	elif mas == 0 and aiur == 2:
		print(f'You choose {signu}.')
		print(tu)
		print(f'Computer chose {sign}.')
		print(comp)
		print('You Win :((')
		
	elif mas == 2 and aiur == 0:
		print(f'You choose {signu}.')
		print(tu)
		print(f'Computer chose {sign}.')
		print(comp)
		print('You Lose :((')
	
	elif mas > aiur:
		print(f'You choose {signu}.')
		print(tu)
		print(f'Computer chose {sign}.')
		print(comp)
		print('You Lose :((')
	
	elif mas < aiur:
		print(f'You choose {signu}.')
		print(tu)
		print(f'Computer chose {sign}.')
		print(comp)
		print('You Lose :((')
	
	

