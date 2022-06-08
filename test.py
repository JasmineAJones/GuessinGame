import random

##Learn more about hashmaps

print("Options: ")
hashbrowns={1:['green','blue'], 2:['white','yellow'], 3:['pink','purple']}

for number in hashbrowns:
    for i in range(2):
        print(hashbrowns[number][i])
    
print("--------------")
z = input("Please guess a color from list above: ")


x = hashbrowns[int(random.uniform(1,4))][int(random.uniform(0,2))]
y = hashbrowns[int(random.uniform(1,4))][int(random.uniform(0,2))]


if x == y:
    if x == z:
        print("Correct! The answer was "+x)
    else:
        print("Wrong...the answer was "+x)

else:
    if x == z or y == z:
        print("Correct! The answer was "+x+" or "+y)
    else:
        print("Wrong...the answer was "+x+" or "+y)

