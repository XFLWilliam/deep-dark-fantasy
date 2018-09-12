
x = list(range(101))
x.pop(0)
for c in x:
    i = c**3
    i = str(i)

    b = 0
    sum = 0
    while b < len(i):
        sum = sum + int(i[b])
        b = b+1
    if sum == c:
        print(c)

