import random


def sort(a, b, c):
    if a > b:
        tempt = a
        a = b
        b = tempt
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        tem = b
        b = c
        c = tem
    return [a, b, c]


def guess(num):
    a = 0
    while a < 10:
        a = a+1
        enter = input("Please enter three number:")
        if enter == num:
            print("Absolutely right")
            return
        x = int(enter[0])
        y = int(enter[1])
        z = int(enter[2])
        liste = sort(x, y, z)
        x1 = int(num[0])
        y1 = int(num[1])
        z1 = int(num[2])
        listn = sort(x1, y1, z1)

        if liste[0] == listn[0] and liste[1]==listn[1]and liste[2]==listn[2]:
            print("number is correct")
        else:
            print("error")
    print("Over")
    return


number = random.randint(100, 999)
num = str(number)
print("when I say：         It means:")
print("error                The 3 numbers are not in the mystical numbers")
print("number is correct    The number is right , but the position is not right")
print("Absolutely right     Numbers is right and the position also right")
guess(num)
