import random


def guessing(goal):
    guess = input("请输入:")
    num = int(guess)

    if num == goal:
        print('Congratulations!')
        return
    elif num > goal:
        print("Too big")
        guessing(goal)
    elif num < goal:
        print("Too small")
        guessing(goal)


number = random.randint(0, 100)
print('Please guess number between 0 and 100')
guessing(number)



