# number gusssing game

import random
randNo = random.randint(1, 100)
guess = 0
# n = None
while True:
    n = int(input("enter a number guess between 1 to 100:"))
    guess +=1
    if n == randNo:
        print("you chose a right number")
        break
    elif n > randNo:
        print('you choose biggest number plz chose smallest number')
    else:
        print('you choose smallest number plz chose biggest number')

print(f'you choose a {guess} times')

