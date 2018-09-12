def slice(a, x, y):
    while x < y:
        a[x] = a[x].title()
        print(a[x], end=" ")
        x = x + 1
    print()


players = ["charles", "martina", "michael", "florence", "eli"]
slice(players, 1, 4)
slice(players, 0, 2)
