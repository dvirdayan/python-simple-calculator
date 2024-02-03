from tkinter import *
field_text = ''
ans = False


def remove():
    global field_text
    field_text = field_text[:-1]
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


def add_to_field(newstr):
    global field_text
    global ans
    if ans and newstr.isnumeric():
        field_text = ""
    ans = False
    field_text = field_text + str(newstr)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


def calculate():
    global field_text
    global ans
    ans = True
    try:
        field_text = str(eval(field_text)).rstrip(".0")
    except Exception as error:
        field_text = str(error)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")


window = Tk()
window.geometry('185x168')
window.title("calculator")

field = Text(window, width=22, height=2)
field.grid(row=1, column=1, columnspan=4)

# text buttons
b0 = Button(window, text='0', width=5, command=lambda: add_to_field('0'))
b0.grid(row=5, column=1)
b1 = Button(window, text='1', width=5, command=lambda: add_to_field('1'))
b1.grid(row=4, column=1)
b2 = Button(window, text='2', width=5, command=lambda: add_to_field('2'))
b2.grid(row=4, column=2)
b3 = Button(window, text='3', width=5, command=lambda: add_to_field('3'))
b3.grid(row=4, column=3)
b4 = Button(window, text='4', width=5, command=lambda: add_to_field('4'))
b4.grid(row=3, column=1)
b5 = Button(window, text='5', width=5, command=lambda: add_to_field('5'))
b5.grid(row=3, column=2)
b6 = Button(window, text='6', width=5, command=lambda: add_to_field('6'))
b6.grid(row=3, column=3)
b7 = Button(window, text='7', width=5, command=lambda: add_to_field('7'))
b7.grid(row=2, column=1)
b8 = Button(window, text='8', width=5, command=lambda: add_to_field('8'))
b8.grid(row=2, column=2)
b9 = Button(window, text='9', width=5, command=lambda: add_to_field('9'))
b9.grid(row=2, column=3)
bdot = Button(window, text='.', width=5, command=lambda: add_to_field('.'))
bdot.grid(row=5, column=2)
bobracket = Button(window, text='(', width=5, command=lambda: add_to_field('('))
bobracket.grid(row=6, column=1)
bcbracket = Button(window, text=')', width=5, command=lambda: add_to_field(')'))
bcbracket.grid(row=6, column=2)

# operation buttons
bdiv = Button(window, text='/', width=5, command=lambda: add_to_field('/'))
bdiv.grid(row=2, column=4)
btimes = Button(window, text='*', width=5, command=lambda: add_to_field('*'))
btimes.grid(row=3, column=4)
bminus = Button(window, text='-', width=5, command=lambda: add_to_field('-'))
bminus.grid(row=4, column=4)
bplus = Button(window, text='+', width=5, command=lambda: add_to_field('+'))
bplus.grid(row=5, column=4)
bequal = Button(window, text='=', width=12, command=calculate)
bequal.grid(row=6, column=3, columnspan=2)

bclear = Button(window, text='c', width=5, command=clear)
bclear.grid(row=5, column=3)

window.mainloop()
