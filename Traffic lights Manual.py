from tkinter import *

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


obj = Tk()
obj.geometry('280x400')
obj.title('Traffic Light with Manual Control')
obj.configure(bg='white')


button1 = Button(obj, text='RED', font=('Calibri', 15),bg='gray', fg='white', width='11', height='2', command=red)
button1.grid(row='1', column='1')

canvas1 = Canvas(obj, height=130, bg='lightblue')
canvas1.grid(row='1', column='2')

button2 = Button(obj, text='YELLOW', font=('Calibri', 15),bg='gray', fg='white', width='11', height='2', command=yellow)
button2.grid(row='2', column='1')

canvas2 = Canvas(obj, height=130, bg='lightblue')
canvas2.grid(row='2', column='2')

button3 = Button(obj, text='GREEN', font=('Calibri', 15),bg='gray', fg='white', width='11', height='2', command=green)
button3.grid(row='3', column='1')

canvas3 = Canvas(obj, height=130, bg='lightblue')
canvas3.grid(row='3', column='2')

obj.mainloop()
