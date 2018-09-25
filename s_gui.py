import random
from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox

class Hero:
	def __init__(self, name, health=100):
		self.name = name
		self.abilities = list()
		self.armors = list()
		self.start_health = health
		self.health = health
		self.deaths = 0
		self.kills = 0

	def add_ability(self, ability):
		self.abilities.append(ability)
	
	def attack(self):
		total = 0
		for i in self.abilities:
			total += i.attack()
		return total

	def defend(self):
		total = 0
		for i in self.armors:
			total += i.defend()
		return total

	def take_damage(self, damage_amt):
		self.health -= damage_amt
		if self.health < 0:
			self.deaths += 1
		return self.deaths

	def add_kill(self, num_kills):
		self.kills += num_kills

class Abilities:
	def __init__(self, name, strength):
		self.name = name
		self.strength = strength

	def attack(self):
		low = self.strength // 2
		return random.randint(low, self.strength)

	def update_attack(self, attack_strenght):
		self.strength = attack_strength

class Weapon(Abilities):
	def attack(self):
		return random.randint(0, self.strength)

class Armor:
	def __init__(self, name):
		self.name = name
		self.defense = random.randint(0, 100)

	def defend(self):
		return random.randint(0, defense)

class Team:
	def __init__(self, team_name):
		self.name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		self.heroes.append(Hero)

	def remove_hero(self, name):
		self.heroes.remove(name)

	def find_hero(self, name):
		for i in self.heroes:
			if i.name == name:
				return i
		return 0

	def view_all_heroes(self):
		for i in self.heroes:
			print(i.name)

	def update_kills(self, kills):
		rm = kills % len(self.heroes)
		self.heroes[0].add_kill(rm)
		kills = kills / len(self.heroes)
		for i in self.heroes:
			i.add_kill(kills)

	def attack(self, other_team):
		total_attack = 0
		kills = 0
		for i in self.heroes:
			total_attack += i.attack()
		kills = other_team.defend(total_attack)
		self.update_kills(kills)
	
	def deal_damage(self, damage):
		damage = damage / len(self.heroes)
		kills = 0
		for i in self.heroes:
			kills += i.take_damage(damage)
		return kills

	def defend(self, damage_amt):
		total_defense = 0
		kills = 0
		for i in self.heroes:
			total_defense += i.defend()
		damage_amt -= total_defense
		if damage_amt > 0:
			kills += self.deal_damage(damage_amt)
		return kills

	def revive_heroes(self, health=100):
		for i in self.heroes:
			i.health = health

	def stats(self):
		for i in self.heroes:
			print(i.name + " K/D: " + str(i.kills) + "/" + str(i.deaths))

class Arena:
	def __init__(self):
		self.team_one = None
		self.team_two = None
		self.heroes = list()
		self.i = 0
		
	def user_input(self, prompt):
		user_input = input(prompt)
		return user_input

	def add_heroes(self):
		self.heroes.append(Hero(txt.get()))
		ability_name1 = txt2.get(),
		power1 = len(ability_name1) * random.randint(1, 5) * 10
		ability1 = Abilities(ability_name1, power1)
		self.heroes[self.i].add_ability(ability1)
		weapon1 = Weapon(txt3.get(), random.randint(1, 5) * 10)
		self.heroes[self.i].add_ability(weapon1)
		if chk_state == True:
			armor = Armor(armors)
			self.heroes[self.i].armors.append(armor)

	def create_team(self):
		self.team_one = Team(txt3.get())
		self.team_two = Team(txt4.get())

	def team_battle(self):
		deaths1 = 0
		deaths2 = 0
		
		while deaths1 < len(self.team_one.heroes) or deaths2 < len(self.team_two.heroes):
			self.team_one.attack(self.team_two)
			self.team_two.attack(self.team_one)
			for i in self.team_one.heroes:
				deaths1 += i.deaths
			for i in self.team_two.heroes:
				deaths2 += i.deaths

	def show_stats(self):
		print(self.team_one.name + " stats:")
		self.team_one.stats()
		print(self.team_two.name + " stats:")	
		self.team_two.stats()

arena = Arena()
#arena.build_team_one()
#arena.build_team_two()
#arena.team_battle()
#arena.show_stats()

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
tab_control.add(tab2, text = 'Create Teams', state=DISABLED)
tab_control.add(tab3, text = 'Arena', state=DISABLED)
tab_control.grid(row=1)

##

lbl = Label(tab1, text="Hero name: ", font=("Arial Bold", 16))
lbl1 = Label(tab1, text="Ability name: ", font=("Arial Bold", 16))
lbl2 = Label(tab1, text="Weapon name: ", font=("Arial Bold", 16))

lbl3 = Label(tab1, text="1st team name: ", font=("Arial Bold", 16))
lbl4 = Label(tab1, text="2nd team name: ", font=("Arial Bold", 16))

lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)

lbl3.grid(column=0, row=7)
lbl4.grid(column=0, row=8)

tree1 = ttk.Treeview(tab3)

tree1["columns"]=("one","two")
tree1.column("one", width=100)
tree1.column("two", width=100)
tree1.heading("one", text="Kills")
tree1.heading("two", text="Deaths")

#id1 = tree1.insert("", 1, "dir1", text="Dir 1")
#id2 = tree1.insert("", 1, "dir2", text="Dir 2")
#tree1.insert(id1, "end", "stuff", text="sub dir 1", values=("2A","2B"))
#tree1.insert(id2, "end", "stuff2", text="sub dir 2", values=("2A","2B"))

tree1.grid(column=0, row=1)

a = 0

def submit_hero():
	global a
	if txt.get() == '' or txt1.get() == '' or txt2.get() == '':
		messagebox.showwarning('Error', 'Please fill in all blanks')
	else:
		arena.add_heroes()
		listbox.insert(arena.i, arena.heroes[arena.i].name)
		btn2.configure(state='normal')
		messagebox.showinfo('Hero Added', 'Hero ' + arena.heroes[arena.i].name + ' was created\nStrength: ' + str(arena.heroes[arena.i].abilities[0].strength))
		arena.i += 1
		a += 1

def create_teams():
	global a
	if txt3.get() == '' or txt4.get() == '':
		messagebox.showwarning('Error', 'Please fill in all blanks')
	else:
		arena.create_team()
		rad1.configure(text = arena.team_one.name)
		rad2.configure(text = arena.team_two.name)
		globals()["id1"] = tree1.insert("", 0, "dir1", text = arena.team_one.name)
		globals()["id2"] = tree1.insert("", 1, "dir2", text = arena.team_two.name)
		btn2.configure(state=DISABLED)
		if a > 0:
			tab_control.tab(tab2, state='normal')
			tab_control.tab(tab3, state='normal')

def add_hero():
	name = listbox.get(listbox.curselection())
	for i in arena.heroes:
		if i.name == name:
			hero = i
	if selected.get() == 1:
		arena.team_one.add_hero(hero)
		tree1.insert(id1, END, text=hero.name, values=(hero.kills, hero.deaths))
	elif selected.get() == 2:
		arena.team_two.add_hero(hero)
		tree1.insert(id2, END, text=hero.name, values=(hero.kills, hero.deaths))
	listbox.delete(listbox.curselection())

def battle():
	arena.team_battle()
	arena.show_stats()
	tree1.configure()

#sep = ttk.Separator(tab1, orient=HORIZONTAL)
#sep.grid(row=6, columnspan=8, sticky=W+E)

btn = Button(tab1, text="Create Hero", command=submit_hero)
btn2 = Button(tab1, text="Create Teams", state=DISABLED, command=create_teams)
btn3 = Button(tab2, text='Add Hero', command=add_hero)
btn4 = Button(tab3, text="Battle!", command=battle)

btn.grid(column=0, row=5, padx=20, pady=20)
btn2.grid(column=0, row=9, padx=20, pady=20)
btn3.grid(column=0, row=6)
btn4.grid(column=0, row=3, padx=15, pady=15)

selected = IntVar()
rad1 = Radiobutton(tab2, text='', value=1, variable=selected)
rad2 = Radiobutton(tab2, text='', value=2, variable=selected)

rad1.grid(column=0, row=4, padx=10)
rad2.grid(column=0, row=5, padx=10)

listbox = Listbox(tab2)
listbox.grid(column=0, row=1)

txt = Entry(tab1, width=16)
txt1 = Entry(tab1, width=16)
txt2 = Entry(tab1, width=16)

txt3 = Entry(tab1, width=16)
txt4 = Entry(tab1, width=16)

txt.grid(column=1, row=0)
txt1.grid(column=1, row=1)
txt2.grid(column=1, row=2)

txt3.grid(column=1, row=7)
txt4.grid(column=1, row=8)

#combo = Combobox(window)
#combo['values'] = (1, 2, 3, 4, 5, "Text")
#combo.current(1)
#combo.grid(column=0, row=2)

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(tab1, text='Add Armor', var=chk_state)
chk.grid(column=0, row=3, padx=12, pady=12)

txt.focus()
window.mainloop()
