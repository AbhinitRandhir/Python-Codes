#create Radio buttons
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry('350x200')
rad1 = Radiobutton(window,text='Male', value=1)
rad2 = Radiobutton(window,text='Female', value=2)
rad3 = Radiobutton(window,text='Transgender', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
#m = Message(window, text="this is a message!")
#m.grid(column=2,row = 4)
# m.config(bg="red")
window.mainloop()