from Tkinter import *
import tkMessageBox
import json

with open("types.json") as f:
	data = json.load(f)

types = data.keys()
types = [str(t) for t in types]
maxLengthType = max([len(n) for n in types])
typesSpaces = [t.ljust(maxLengthType, ' ') for t in types]

counter = {}
historyEntry = ["normal", "normal"]
historyEntry2 = ["normal", "normal"]
historyEntry3 = ["normal", "normal"]
historyEntry4 = ["normal", "normal"]
historyEntry5 = ["normal", "normal"]
historyEntry6 = ["normal", "normal"]

def getWeakDefenders(attacker):
	return [str(x) for x in data[attacker]["super_effective"]]

def validate(string_to_validate):
	string_to_validate = string_to_validate.strip()
	if string_to_validate in types:
		return string_to_validate
	elif string_to_validate == "":
		return "normal"
	else:
		return ""

window = Tk()
window.title("Type Coverage Team Builder")
window.geometry('500x350')

r = 0
c = 0
lbl = list()
for i in range(len(typesSpaces)):
	lbl.append(Label(window, text=typesSpaces[i], bg="White", font=("Times New Roman", 14)))
	counter[lbl[i]] = 0
	if c < 6:
		lbl[i].grid(column=c, row=r)
	else:
		c = 0
		r += 1
		lbl[i].grid(column=c, row=r)
	c += 1

def clickedTypeButton():
	attacker1 = typeEntry_1.get()
	attacker2 = typeEntry_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 1)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel = Label(window, text="Enter type: ")
typeEntry_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry_2 = Entry(window, bd=5, width=maxLengthType)
typeButton = Button(window, text="Enter", command=clickedTypeButton)
typeLabel.grid(column=0, row=r)
typeEntry_1.grid(column=1, row=r)
typeEntry_2.grid(column=2, row=r)
typeButton.grid(column=3, row=r)

def clickedTypeButton2():
	attacker1 = typeEntry2_1.get()
	attacker2 = typeEntry2_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 2)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel2 = Label(window, text="Enter type: ")
typeEntry2_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry2_2 = Entry(window, bd=5, width=maxLengthType)
typeButton2 = Button(window, text="Enter", command=clickedTypeButton2)
typeLabel2.grid(column=0, row=r)
typeEntry2_1.grid(column=1, row=r)
typeEntry2_2.grid(column=2, row=r)
typeButton2.grid(column=3, row=r)

def clickedTypeButton3():
	attacker1 = typeEntry3_1.get()
	attacker2 = typeEntry3_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 3)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel3 = Label(window, text="Enter type: ")
typeEntry3_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry3_2 = Entry(window, bd=5, width=maxLengthType)
typeButton3 = Button(window, text="Enter", command=clickedTypeButton3)
typeLabel3.grid(column=0, row=r)
typeEntry3_1.grid(column=1, row=r)
typeEntry3_2.grid(column=2, row=r)
typeButton3.grid(column=3, row=r)

def clickedTypeButton4():
	attacker1 = typeEntry4_1.get()
	attacker2 = typeEntry4_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 4)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel4 = Label(window, text="Enter type: ")
typeEntry4_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry4_2 = Entry(window, bd=5, width=maxLengthType)
typeButton4 = Button(window, text="Enter", command=clickedTypeButton4)
typeLabel4.grid(column=0, row=r)
typeEntry4_1.grid(column=1, row=r)
typeEntry4_2.grid(column=2, row=r)
typeButton4.grid(column=3, row=r)

def clickedTypeButton5():
	attacker1 = typeEntry5_1.get()
	attacker2 = typeEntry5_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 5)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel5 = Label(window, text="Enter type: ")
typeEntry5_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry5_2 = Entry(window, bd=5, width=maxLengthType)
typeButton5 = Button(window, text="Enter", command=clickedTypeButton5)
typeLabel5.grid(column=0, row=r)
typeEntry5_1.grid(column=1, row=r)
typeEntry5_2.grid(column=2, row=r)
typeButton5.grid(column=3, row=r)

def clickedTypeButton6():
	attacker1 = typeEntry6_1.get()
	attacker2 = typeEntry6_2.get()
	checkChangeAndUpdateCounter([attacker1, attacker2], 6)
	attacker1 = validate(attacker1)
	attacker2 = validate(attacker2)
	if attacker1 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 1!")
	elif attacker2 == "":
		tkMessageBox.showerror(title="ERROR", message="Invalid type entry 2!")
	else:
		typesCovered = getWeakDefenders(attacker1)
		typesCovered.extend(getWeakDefenders(attacker2))
		for t in typesCovered:
			lbl[types.index(t)].config(bg="Black")
			counter[lbl[types.index(t)]] += 1

r += 1
typeLabel6 = Label(window, text="Enter type: ")
typeEntry6_1 = Entry(window, bd=5, width=maxLengthType)
typeEntry6_2 = Entry(window, bd=5, width=maxLengthType)
typeButton6 = Button(window, text="Enter", command=clickedTypeButton6)
typeLabel6.grid(column=0, row=r)
typeEntry6_1.grid(column=1, row=r)
typeEntry6_2.grid(column=2, row=r)
typeButton6.grid(column=3, row=r)

def checkChangeAndUpdateCounter(entry_pair, index):
	if index == 1:
		if entry_pair[0] != historyEntry[0]:
			typeEntry1 = getWeakDefenders(historyEntry[0])
			historyEntry[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry[1]:
			typeEntry2 = getWeakDefenders(historyEntry[1])
			historyEntry[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

	elif index == 2:
		if entry_pair[0] != historyEntry2[0]:
			typeEntry1 = getWeakDefenders(historyEntry2[0])
			historyEntry2[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry2[1]:
			typeEntry2 = getWeakDefenders(historyEntry2[1])
			historyEntry2[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

	elif index == 3:
		if entry_pair[0] != historyEntry3[0]:
			typeEntry1 = getWeakDefenders(historyEntry3[0])
			historyEntry3[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry3[1]:
			typeEntry2 = getWeakDefenders(historyEntry3[1])
			historyEntry3[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

	elif index == 4:
		if entry_pair[0] != historyEntry4[0]:
			typeEntry1 = getWeakDefenders(historyEntry4[0])
			historyEntry4[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry4[1]:
			typeEntry2 = getWeakDefenders(historyEntry4[1])
			historyEntry4[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

	elif index == 5:
		if entry_pair[0] != historyEntry5[0]:
			typeEntry1 = getWeakDefenders(historyEntry5[0])
			historyEntry5[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry5[1]:
			typeEntry2 = getWeakDefenders(historyEntry5[1])
			historyEntry5[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

	elif index == 6:
		if entry_pair[0] != historyEntry6[0]:
			typeEntry1 = getWeakDefenders(historyEntry6[0])
			historyEntry6[0] = entry_pair[0]
			for t in typeEntry1:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")

		if entry_pair[1] != historyEntry6[1]:
			typeEntry2 = getWeakDefenders(historyEntry6[1])
			historyEntry6[1] = entry_pair[1]
			for t in typeEntry2:
				counter[lbl[types.index(t)]] -= 1
				if counter[lbl[types.index(t)]] <= 0:
					lbl[types.index(t)].config(bg="White")


entries = [
typeEntry_1, typeEntry_2,
typeEntry2_1, typeEntry2_2,
typeEntry3_1, typeEntry3_2,
typeEntry4_1, typeEntry4_2,
typeEntry5_1, typeEntry5_2,
typeEntry6_1, typeEntry6_2
]

def clickedReset():
	for label in lbl:
		label.config(bg="White")
	for e in entries:
		e.delete(0,maxLengthType)
	for x in counter:
		counter[x] = 0

r += 1
resetButton = Button(window, text="Reset", command=clickedReset)
resetButton.grid(column=5, row=r)

window.mainloop()