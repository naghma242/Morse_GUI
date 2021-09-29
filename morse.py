import time
from tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


 
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
## hardware
light = LED(4)

## GUI DEFINITIONS ##
root = Tk()
root.title("Morse Blinker")
e = Entry(root, width = 50)
e.pack()

###EVENT FUCNTIONS
def click():
    label= Label(root) #, text = e.get())
    label.pack()
    print("Hello " + e.get())
    main()
    print("Goodbye!")
    
button = Button(root, text="Enter", command= click)
button.pack()

def dot():
    light.on()
    time.sleep(0.3)
    light.off()
    time.sleep(0.3)

def dash():
    light.on()
    time.sleep(0.9)
    light.off()
    time.sleep(0.3)
    
def main():
    a = e.get().upper()
    for char in a:
        encrypted = encrypt(char)
        for enc_item in encrypted:
            if enc_item == "-":
                dash()
            elif enc_item == ".":
                dot()
        time.sleep(0.3)
        
