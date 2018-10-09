import os
import fnmatch


def bfs(path):
    queue = []
    queue.append(path)

    while len(queue) > 0:
        filePath = queue.pop(-1)

        fileList = os.listdir(filePath)

        for p in fileList:
           next = os.path.join(filePath,p)
           if os.path.isdir(next):
               queue.append(next)
           elif os.path.isfile(next):
               if fnmatch.fnmatch(p,"*.dll"):
                   print(p)


dfs('C:\\')
