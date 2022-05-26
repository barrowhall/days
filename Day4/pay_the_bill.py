import random

name = input('Give me evrybody names, separated by comma: ')

one = name.split(', ')

print(one)

numb = random.randint(0, len(one))

print(numb)
