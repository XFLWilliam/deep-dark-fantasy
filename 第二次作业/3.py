import os
import fnmatch


def dfs(path):
    stack = []
    stack.append(path)

    while len(stack) > 0:
        filePath = stack.pop()

        fileList = os.listdir(filePath)

        for p in fileList:
           next = os.path.join(filePath,p)
           if os.path.isdir(next):
               stack.append(next)
           elif os.path.isfile(next):
               if fnmatch.fnmatch(p,"*.dll"):
                   print(p)


dfs('C:\\')
