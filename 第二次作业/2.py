class Node:
    def __init__(self, name):
        self.nextArr = []
        self.name = name

    def add_next(self, arr):
        for i in arr:
            self.nextArr.append(i)


stack = []
store = []


def dfs(start, end):

    stack.append(start)
    store.append(start)

    while len(stack) != 0:
        tempt = stack.pop()
        if tempt.name == end.name:
            return tempt.name
        else:
            for i in tempt.nextArr:
                if i not in store:
                    stack.append(i)
                    store.append(i)


if __name__ == '__main__':
    you = Node("you")
    bob = Node("bob")
    alice = Node("alice")
    claire = Node("claire")
    thom = Node("thom")
    jonny = Node("jonny")
    peggy = Node("peggy")
    anuj = Node("anuj")

    you.add_next([bob, alice, claire])
    alice.add_next([peggy])
    bob.add_next([peggy, anuj])
    claire.add_next([thom, jonny])


print(dfs(you, thom))
