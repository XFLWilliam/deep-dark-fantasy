from tkinter import *


def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Calculator(Frame):
    def __init__(self):

        Frame.__init__(self)

        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculater')

        display = StringVar()
        Entry(self, relief=SUNKEN,
              textvariable=display).pack(side=TOP, expand=YES,
                                         fill=BOTH)

        clearF = frame(self, TOP)
        button(clearF, LEFT, 'C', lambda w=display: w.set(''))
        button(clearF, LEFT, 'CE')

        operator = frame(self, TOP)
        for char in '+-*/=':
            if char == '=':
                btn = button(operator, LEFT, char)
                btn.bind('<ButtonRelease - 1>', lambda e, s=self, w=display: s.calc(w), '+')

            else:
                btn = button(operator, LEFT, char, lambda w=display, s='%s' % char: w.set(w.get() + s))

        for key in ('1234', '5678', '90'):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()


