from tkinter import *
from time import sleep

def red():
    canvas1.create_oval(120, 120, 50, 50, fill='red', outline='black', width='3')
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')

def yellow():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')
    canvas2.create_oval(120, 120, 50, 50, fill='yellow', outline='black', width='3')
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')

def green():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='black', width='3')
    canvas3.create_oval(120, 120, 50, 50, fill='green', outline='black', width='3')

count = 25
def start():
    counter(count)

def new(c):
    if c>15:
        red()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c>10 and c<=15:
        yellow()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c>0 and c<=10:
        green()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(c)
    elif c==0:
        count = 25
        red()
        e.config(text=c)
        obj.update()
        sleep(1)
        counter(count)

def counter(cou):
    if cou>0:
        cou = cou-1
        new(cou)

obj = Tk()
obj.geometry('500x600')
obj.title('Traffic Light - Automatic')
obj.configure(bg='white')
e = Label(obj, font=('Arial', 15))
e.pack()

canvas1 = Canvas(obj, bg='black', height='150', width='150')
canvas1.pack()

canvas2 = Canvas(obj, bg='black', height='150', width='150')
canvas2.pack()

canvas3 = Canvas(obj, bg='black', height='150', width='150')
canvas3.pack()

button1 = Button(obj, text='START', command=start, font=('Arial', 15), bg='blue', fg='black', height='2', width='25')
button1.pack()

obj.mainloop()
