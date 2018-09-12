def revsort(a, b, c):

    if(a < b):
        x = a
        a = b
        b = x
    if(b < c):
        x = b
        b = c
        c = x
    if(a < c):
        x = a
        a = c
        c = x

    return a, b, c


a = int(input())
b = int(input())
c = int(input())

print(revsort(a, b, c))


