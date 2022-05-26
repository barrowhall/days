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

aiur = random.randint(0, 2)

comp = lista[aiur]
tu = lista[mas]

if mas == aiur:
	print(comp)
	print('Computer chose.')
	print(tu)
	print('It is a tie ===')

elif mas == 0 and aiur == 2:
	print(comp)
	print('Computer chose.')
	print(tu)
	print('You Win :((')
	
elif mas == 2 and aiur == 0:
	print(comp)
	print('Computer chose.')
	print(tu)
	print('You Lose :((')

elif mas > aiur:
	print(comp)
	print('Computer chose.')
	print(tu)
	print('You Lose :((')

elif mas < aiur:
	print(comp)
	print('Computer chose.')
	print(tu)
	print('You Lose :((')

else:
	print('Not a choice , You Lose :((')




