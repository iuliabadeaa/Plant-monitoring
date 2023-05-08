from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Plant monitoring")
root.geometry("500x500")
root.resizable(True,True)
root.configure(backgroun="#EDF1D6")
frame = Frame(root)
frame.pack()
img = ImageTk.PhotoImage(Image.open("plant.png"))
label = Label(frame, image = img)
label.configure(backgroun="#EDF1D6")
frame.place(x=10,y=50)
label.pack()

mainloop()