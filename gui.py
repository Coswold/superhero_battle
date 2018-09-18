from tkinter import *
from tkinter import Menu
from tkinter import ttk

window = Tk()
window.title("Hero Battle!")
window.geometry('350x200')

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

tab_control.add(tab1, text = 'Home')
tab_control.add(tab2, text = 'Create Team')
tab_control.grid(row=1)

##

lbl = Label(tab1, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

def clicked():
	res = "Welcome to " + txt.get()
	lbl.configure(text= res)

btn = Button(tab1, text="Click Me", command=clicked)
btn.grid(column=0, row=2)

txt = Entry(tab1,width=10)
txt.grid(column=1, row=2)

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
