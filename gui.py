from tkinter import *
from PIL import Image, ImageTk
from pyfirmata import *
import time

import serial.tools.list_ports 
import serial



ser = serial.Serial('COM7', 9600) # Specificați portul serial și viteza de transmisie
ser.enableUSBDetection = True

while True:
    line = ser.readline().decode('utf-8').rstrip() # Citirea datelor de la portul serial
    print(line)

# serialInst=serial.Serial('COM7',9600,timeout=1)
# time.sleep(2)

# serialInst.write("Hello Arduino!")

# for i in range(600):
#     line=serialInst.readline().decode("utf-8")
#     print(line)


#ports=serial.tools.list_ports.comports()

# portList=[]

# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))

# val=input("select Port: COM")

# for x in range(0,len(portList)):
#     if portList[x].startswith("COM" + str(val)):
#         portVar="COM"+str(val)
#         print(portList[x])

# serialInst.baudrate=9600
# serialInst.port=portVar
# serialInst.open()

# while True:
#     if serialInst.in_waiting:
#         packet=serialInst.readline()
#         print(packet.decode("utf"))



# menu=Tk()
# menu.title("Plant monitoring")
# menu.geometry("500x500")
# menu.resizable(True,True)
# menu.configure(backgroun="#EDF1D6")
# greeting=Label(menu,text="Hello! How may I help you today?")
# greeting.configure(background="#EDF1D6",font="40,helvetica",foreground="#617A55")
# greeting.place(x=20,y=20)

# def show_temp():



# root=Tk()
# root.title("Plant monitoring")
# root.geometry("500x500")
# root.resizable(True,True)
# root.configure(backgroun="#EDF1D6")
# frame = Frame(root)
# frame.pack()
# img = ImageTk.PhotoImage(Image.open("plant.png"))
# label = Label(frame, image = img)
# label.configure(backgroun="#EDF1D6")
# frame.place(x=10,y=50)
# label.pack()
# temperature=Label(root,text="TEMPERATURE")
# temperature.place(x=200,y=100)
# temperature.configure(background="#EDF1D6",foreground="#617A55",font=40)
# show_temperature=Label(root,command=show_temp)

mainloop()