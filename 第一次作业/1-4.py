
fruits = ['apple', 'pear', 'orange', 'banana', 'kiwi']

for fruit in fruits:
    if fruit == 'apple':
        print('I found it!')

fruits.append('mandarin')
fruits.append('pineapple')

num = []
for fruit in fruits:
    a = len(fruit)
    num.append(a)

x = 0
while x < len(num):
    print('{0}, has, {1}, letters'.format(fruits[x], num[x]))
    x = x + 1




