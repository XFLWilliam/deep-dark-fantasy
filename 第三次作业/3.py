from tkinter import *  # 导入 Tkinter 库

root = Tk()
root.title('coding')
A = ['C', 'python', 'php', 'html', 'SQL', 'java']
B = ['CSS', 'jQuery', 'Bootstrap']

list1 = Listbox(root)  # 创建两个列表组件
list2 = Listbox(root)

for item in A:
    list1.insert(0, item)

for item in B:
    list2.insert(0, item)

list1.pack()
list2.pack()
root.mainloop()  # 进入消息循环
