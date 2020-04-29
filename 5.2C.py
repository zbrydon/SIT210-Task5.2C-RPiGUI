from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware

ledRed = LED(14)
ledGreen = LED(15)
ledBlue = LED(18)


## GUI DEFINITIONS ##

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = "bold")

##Event functions ##

def ledRedToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledRedButton["text"] = "Turn Red LED on"
    else:
        ledRed.on()
        ledRedButton["text"] = "Turn Red LED off"
def ledGreenToggle():
    if ledGreen.is_lit:
        ledGreen.off()
        ledGreenButton["text"] = "Turn Green LED on"
    else:
        ledGreen.on()
        ledGreenButton["text"] = "Turn Green LED off"
def ledBlueToggle():
    if ledBlue.is_lit:
        ledBlue.off()
        ledBlueButton["text"] = "Turn Blue LED on"
    else:
        ledBlue.on()
        ledBlueButton["text"] = "Turn Blue LED off"
def close():
    RPi.GPIO.cleanup()
    win.destroy()
                     

## Widgets ##
ledRedButton = Button(win, text = 'Turn Red LED On', font = myFont,command = ledRedToggle, bg = 'red' , height = 1, width = 24)
ledRedButton.grid(row = 0, column = 1)

ledGreenButton = Button(win, text = 'Turn Green LED On', font = myFont,command = ledGreenToggle, bg = 'green' , height = 1, width = 24)
ledGreenButton.grid(row = 2, column = 1)


ledBlueButton = Button(win, text = 'Turn Blue LED On', font = myFont,command = ledBlueToggle, bg = 'blue' , height = 1, width = 24)
ledBlueButton.grid(row = 3, column = 1)


exitButton = Button(win , text = 'Exit' , font = myFont , command = close, bg = 'white' , height = 1 , width = 10)
exitButton.grid(row = 4, column = 1)


win.protocol("WM_DELETE_WINDOW" , close)

win.mainloop()













