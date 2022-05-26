import random

name = input('Give me everybody names, separated by comma: ')

one = name.split(', ')
leni = len(one)

numb = random.randint(0, leni- 1)

print(one[numb].capitalize() + ' is going to pay the meal today.')



