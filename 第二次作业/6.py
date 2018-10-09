openList = []
closeList = []
Path = []


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findmin(start, end):
    dis = 100
    minimum = Node(0, 0)

    for tempt in openList:
        current = abs(end.x - tempt.x) + abs(end.y - tempt.y) + abs(start.x - tempt.x) + abs(start.y - tempt.y)
        if current < dis:
            dis = current
            minimum = tempt
    Path.append(minimum)
    return minimum


def findneigh(a):
    neigh = []
    x = a.x
    y = a.y
    n1 = Node(x+1, y)
    n2 = Node(x-1, y)
    n3 = Node(x, y+1)
    n4 = Node(x, y-1)
    neigh.append(n1)
    neigh.append(n2)
    neigh.append(n3)
    neigh.append(n4)

    return neigh


def asearch(start, end):
    openList.append(start)
    while len(openList) > 0:
        a = findmin(start, end)
        openList.remove(a)
        closeList.append(a)

        neigh = findneigh(a)

        for n in neigh:
            if n != (4, 1)or(4, 2)or(4, 3):
                if n not in openList:
                        openList.append(n)
        for result in openList:
            if result == end:
                return true

    return false


s = Node(2, 3)
e = Node(6, 3)
if asearch(s, e) == true:
    print(Path)
else:
    print("cannot reach")
