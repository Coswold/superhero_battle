from tkinter import *
from tkinter import Menu
from tkinter import ttk

window = Tk()
window.title("Hero Battle!")
window.geometry('500x500')

#menu = Menu(window)
#new_item = Menu(menu)
#new_item.add_command(label='New')
#menu.add_command(label='Menu')
#menu.add_cascade(label='Menu', menu=new_item)
#window.config(menu=menu)

##

tab_control = ttk.Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)

tab_control.add(tab1, text = 'Create Heroes')
tab_control.add(tab2, text = 'Create Teams')
tab_control.add(tab3, text = 'Arena')
tab_control.grid(row=1)

##

lbl = Label(tab1, text="Hero name: ", font=("Arial Bold", 16))
lbl1 = Label(tab1, text="Ability name: ", font=("Arial Bold", 16))
lbl2 = Label(tab1, text="Weapon name: ", font=("Arial Bold", 16))

lbl3 = Label(tab2, text="1st team name: ", font=("Arial Bold", 16))
lbl4 = Label(tab2, text="2nd team name: ", font=("Arial Bold", 16))

lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)

lbl3.grid(column=0, row=1)
lbl4.grid(column=0, row=2)

def clicked():
	res = "Welcome to " + txt.get()
	lbl.configure(text= res)

btn = Button(tab1, text="Submit", command=clicked)
btn2 = Button(tab2, text="Submit", command=clicked)

btn.grid(column=0, row=3)
btn2.grid(column=0, row=3)

txt = Entry(tab1, width=16)
txt1 = Entry(tab1, width=16)
txt2 = Entry(tab1, width=16)

txt3 = Entry(tab2, width=16)
txt4 = Entry(tab2, width=16)

txt.grid(column=1, row=0)
txt1.grid(column=1, row=1)
txt2.grid(column=1, row=2)

txt3.grid(column=1, row=1)
txt4.grid(column=1, row=2)

#combo = Combobox(window)
#combo['values'] = (1, 2, 3, 4, 5, "Text")
#combo.current(1)
#combo.grid(column=0, row=2)

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(tab1, text='Choose', var=chk_state)
chk.grid(column=0, row=4)

txt.focus()
window.mainloop()
