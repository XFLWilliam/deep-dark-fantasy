def chibit():
    x = 0
    leg = 0

    while leg < 94:
        x = x + 1
        leg = 4*x+2*(35-x)
    return x


result = chibit()
print(result)
