import time
import random

name = None
while not name:
    name = input('hey gimme sumn to call you: ')

display = [f'hey {name} i hope you do good today!', f'i like your {name}',
           f'wow ready to grind now now {name}?', f'no pain no gain {name}', 'another basic bullshit motivating quote']
print(random.choice(display), '🎀' * 10)

Range = int(input('how many chores you have today?  '))
b = 'no'

stuff = []


def chore():
    task = input(f'what is on your mind {name}? ')
    stuff.append(task)


for i in range(Range):
    chore()

print(
    '_____________________________________________________________________________'  f'\n total chores: \n {stuff}')

for j in stuff:
    d = (input('did you do it? '))
    print(j, d)
    if d == b.lower():
        continue
