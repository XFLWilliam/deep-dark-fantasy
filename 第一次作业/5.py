def half_squared(x=[]):
    a = 0
    while a < len(x):
        x[a] = x[a]*x[a]/2
        a = a + 1
    return x


print(half_squared([3, 3]) == [4.5, 4.5])

