def cost(i, k):
    if k == 0:
        return i
    elif k == 1:
        return i/2
    elif k == 2:
        return i+2

start = 2
goal = 85
f = [-1]*(goal+1)
f[2] = 0
i = 0
while i <= 43:

    for k in range(3):

        if 2 * i + k <= 85:

            if f[2 * i + k] == -1:
                f[2 * i + k] = f[i] + cost(i, k)

            elif f[2 * i + k] > f[i] + cost(i, k):
                    f[2 * i + k] = f[i] + cost(i, k)

    i = i+1

print(f[goal])
