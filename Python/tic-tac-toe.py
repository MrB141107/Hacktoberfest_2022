from tkinter import *
from tkinter import font

window = Tk()
window.title('tic-tac-toe')

canvas = Canvas()
canvas.config(height=400, width=400)
canvas.pack()

one = Entry()
one.config(justify='center', font='Georgia')
one.place(x=120, y=80, height=50, width=50)

two = Entry()
two.config(justify='center', font='Georgia')
two.place(x=170, y=80, height=50, width=50)

three = Entry()
three.config(justify='center', font='Georgia')
three.place(x=220, y=80, height=50, width=50)

four = Entry()
four.config(justify='center', font='Georgia')
four.place(x=120, y=130, height=50, width=50)

five = Entry()
five.config(justify='center', font='Georgia')
five.place(x=170, y=130, height=50, width=50)

six = Entry()
six.config(justify='center', font='Georgia')
six.place(x=220, y=130, height=50, width=50)

seven = Entry()
seven.config(justify='center', font='Georgia')
seven.place(x=120, y=180, height=50, width=50)

eight = Entry()
eight.config(justify='center', font='Georgia')
eight.place(x=170, y=180, height=50, width=50)

nine = Entry()
nine.config(justify='center', font='Georgia')
nine.place(x=220, y=180, height=50, width=50)

print(f'{nine.get()}')

window.mainloop()
