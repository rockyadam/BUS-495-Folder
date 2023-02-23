from tkinter import *
# First I will be importing Tkinter
root = Tk()
root.geometry("300x100")
root.title("Need a Nummber?")
root.grid()
# Now I am Creating My GUI Page/Screen

def randnum(event):
	import random
	value =random.randint(1,1000)
	print(value,)
	updateDisplay(value)
# Creating the nummber genertor such as by adding limits (1-1000) and importing random
def updateDisplay(myString):
	displayVariable.set(myString)
# The above code represents the building of the random Nummber Genertor

button_1 = Button(root, text="CLICK IT", background='gold')
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable, background='gold')
displayLabel.pack()
# Here, a button is added to allow the user to use the Genertor
import tkinter
MainW=tkinter.Tk()
MainW.title('Welcome')
MainW.geometry('365x500')
# Here is my seprate code which displays a message seprate from the Generator its self
label = tkinter.Label(MainW, text='Need a Quick Nummber?', font=('Times New Roman', 20))
label.pack(pady=15)
# Here I am creating and adding the message seprate from the Generator
mainloop()
#End code