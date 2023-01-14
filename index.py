import tkinter
from tkinter import *
from tkinter import messagebox
 
expression = ""
def press (num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
 
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
    except:
        equation.set("Avem o eroare!")
        expression = ""
def clear ():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    gui = Tk()
    gui.configure(bg='#438')
    gui.title("Calculator")
    gui.geometry("250x400+300+300")
    gui.resizable(0,0)
    equation =  StringVar()
    expression_field = Entry(gui, width = 20,bg='lightblue', font = ('Times', 12), textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=50, ipady=10)
 
 
 
 
    button1 = Button(gui, text='1', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(1), height=1, width=7).grid(row=2, column=0)
 
    button2 = Button(gui, text='2', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(2), height=1, width=7).grid(row=2, column=1)
 
    button3 = Button(gui, text='3', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(3), height=1, width=7).grid(row=2, column=2)
 
    button4 = Button(gui, text='4', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(4), height=1, width=7).grid(row=3, column=0)
 
    button5 = Button(gui, text='5', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(5), height=1, width=7).grid(row=3, column=1)
 
    button6 = Button(gui, text='6', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(6), height=1, width=7).grid(row=3, column=2)
 
    button7 = Button(gui, text='7', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(7), height=1, width=7).grid(row=4, column=0)
 
    button8 = Button(gui, text='8', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(8), height=1, width=7).grid(row=4, column=1)
 
    button9 = Button(gui, text='9', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(9), height=1, width=7).grid(row=4, column=2)
 
    button0 = Button(gui, text='0', font=("Verdana", 10), relief=GROOVE, fg='black', bg='red', command=lambda:press(0), height=1, width=7).grid(row=5, column=2)
 
    multiply = Button(gui, text='*', font=("Verdana", 10), relief=GROOVE, fg='black', bg='green', command=lambda:press("*"), height=1, width=7).grid(row=7, column=1)
 
    div = Button(gui, text='/', font=("Verdana", 10), relief=GROOVE, fg='black', bg='green', command=lambda:press("/"), height=1, width=7).grid(row=6, column=1)
 
    plus = Button(gui, text='+', font=("Verdana", 10), relief=GROOVE, fg='black', bg='green', command=lambda:press("+"), height=1, width=7).grid(row=6, column=2)
 
    minus = Button(gui, text='-', font=("Verdana", 10), relief=GROOVE, fg='black', bg='green', command=lambda:press("-"), height=1, width=7).grid(row=7, column=2)
 
    equal = Button(gui, text='=', font=("Verdana", 10), relief=GROOVE, fg='black', bg='pink', command=equalpress, height=1, width=7).grid(row=8, column=2)
 
    clear_button = Button(gui, text='clear', font=("Verdana", 10), relief=GROOVE, fg='black', bg='white', command=clear, height=1, width=7).grid(row=8, column=1)
 
    parenthesis= Button(gui, text = '(', font=("Verdana", 10), relief =GROOVE, fg='black', bg='red', command=lambda:press('('), height= 1, width=7).grid(row=5, column=0)
 
    parenthesis2= Button(gui, text = ')', font=("Verdana", 10), relief =GROOVE, fg='black', bg='red', command=lambda:press(')'), height= 1, width=7).grid(row=5, column=1)
 
    dot_button = Button(gui, text = '.', font=("Verdana", 10), relief =GROOVE, fg='black', bg='green', command=lambda:press('.'), height= 1, width=7).grid(row=6, column=0)
 
    percent_button = Button(gui, text = '%', font=("Verdana", 10), relief =GROOVE, fg='black', bg='green', command=lambda:press('%'), height= 1, width=7).grid(row=7, column=0)
 
    gui.mainloop()
