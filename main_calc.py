from tkinter import *

root = Tk()
root.title("Basic Calculator")

disp_val = StringVar()
btn_val = ""
history = " "

#displays key value
def on_key_press(val):
    global btn_val
    btn_val += val
    disp_val.set(btn_val)


#returns result from expression
def on_equal_press():
    global btn_val, history
    try:
        history += '\n' + btn_val
        evaluation = str(eval(btn_val))
        disp_val.set(evaluation)
    except SyntaxError:
        disp_val.set("SyntaxError")
    except ZeroDivisionError:
        disp_val.set("undefined")


def show_history():
    global history
    disp_val.set(history)


#clears the console
def on_clear_press():
    global btn_val
    btn_val = ""
    disp_val.set("")


#button variables
entry = Label(root, textvariable=disp_val, width=40, height=2)
entry.grid(columnspan=4)

btn1 = Button(root, text=1, width=10, height=2)
btn1.bind("<Button-1>", lambda x: on_key_press("1"))
btn1.grid(row=1, column=0)

btn2 = Button(root, text=2, width=10, height=2)
btn2.bind("<Button-1>", lambda x: on_key_press("2"))
btn2.grid(row=1, column=1)

btn3 = Button(root, text=3, width=10, height=2)
btn3.bind("<Button-1>", lambda x: on_key_press("3"))
btn3.grid(row=1, column=2)

btn4 = Button(root, text=4, width=10, height=2)
btn4.bind("<Button-1>", lambda x: on_key_press("4"))
btn4.grid(row=2, column=0)

btn5 = Button(root, text=5, width=10, height=2)
btn5.bind("<Button-1>", lambda x: on_key_press("5"))
btn5.grid(row=2, column=1)

btn6 = Button(root, text=6, width=10, height=2)
btn6.bind("<Button-1>", lambda x: on_key_press("6"))
btn6.grid(row=2, column=2)

btn7 = Button(root, text=7, width=10, height=2)
btn7.bind("<Button-1>", lambda x: on_key_press("7"))
btn7.grid(row=3, column=0)

btn8 = Button(root, text=8, width=10, height=2)
btn8.bind("<Button-1>", lambda x: on_key_press("8"))
btn8.grid(row=3, column=1)

btn9 = Button(root, text=9, width=10, height=2)
btn9.bind("<Button-1>", lambda x: on_key_press("9"))
btn9.grid(row=3, column=2)

btn0 = Button(root, text=0, width=10, height=2)
btn0.bind("<Button-1>", lambda x: on_key_press("0"))
btn0.grid(row=4, column=1)

minus = Button(root, text="-", width=10, height=2)
minus.bind("<Button-1>", lambda x: on_key_press("-"))
minus.grid(row=4, column=2)

divide = Button(root, text="/", width=10, height=2)
divide.bind("<Button-1>", lambda x: on_key_press("/"))
divide.grid(row=4, column=3)

add = Button(root, text="+", width=10, height=2)
add.bind("<Button-1>", lambda x: on_key_press("+"))
add.grid(row=2, column=3)

multiply = Button(root, text="*", width=10, height=2)
multiply.bind("<Button-1>", lambda x: on_key_press("*"))
multiply.grid(row=3, column=3)

clear = Button(root, text="C", width=10, height=2)
clear.bind("<Button-1>", lambda x: on_clear_press())
clear.grid(row=1, column=3)

his_btn = Button(root, text="HIST.", width=10, height=2)
his_btn.bind("<Button-1>", lambda x: show_history())
his_btn.grid(row=4, column=0)

equal = Button(root, text="=", width=10, height=2)
equal.bind("<Button-1>", lambda x: on_equal_press())
equal.grid(row=5, column=3)


root.mainloop()
