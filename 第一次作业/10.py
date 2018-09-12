import random
x = random.randint(1, 10)
y = random.randint(1, 10)
a = x
x = y
y = a

print(x, y)