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

mas = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:  '))

aiur = random.randint(0, 2)

comp = lista[aiur]


if mas == aiur:
	print(rock)
	print('Computer chose Rock.')
	print(rock)
	print('It is a tie ===')

elif mas == 0 and aiur == 2:
	print(scissors)
	print('Computer chose Scissors.')
	print(rock)
	print('You Win :((')

elif mas == 0 and aiur == 1:
	print(scissors)
	print('Computer chose Paper.')
	print(rock)
	print('You Lose :((')

elif mas == 1 and aiur == 2:
	print(scissors)
	print('Computer chose Scissors.')
	print(paper)
	print('You Lose :((')

elif mas == 1 and aiur == 0:
	print(rock)
	print('Computer chose Rock.')
	print(paper)
	print('You Win !!! :))')

elif mas == 2 and aiur == 0:
	print(rock)
	print('Computer chose Rock.')
	print(scissors)
	print('You Lose :((')

elif mas == 2 and aiur == 1:
	print(paper)
	print('Computer chose Paper.')
	print(scissors)
	print('You Win !!!  :))')


