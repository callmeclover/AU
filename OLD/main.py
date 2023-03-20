import keyboard
# import pyautogui
import mouse
import time
import random
import re
import os
import boto3
from zip3 import Zip3

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s

pInputs = ["w", "a", "s", "d", "e", "space", "left", "right", "lclick", "rclick", "ldrag", "rdrag", "thi", "tthank", "tffact", "tnvsmart"]

# x,y = pyautogui.size()
# x,y=int(str(x)),int(str(y))

f = open("OUT/" + urlify(time.ctime(time.mktime(time.localtime()))) + "/" + urlify(time.ctime(time.mktime(time.localtime()))) + "/" + ".txt", "w")

while True:
    cInput = random.choice(pInputs)

    if (cInput == "w"):
        keyboard.press("w")
        time.sleep(random.uniform(0, 5))
        keyboard.release("w")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'W'")
        print("\n("+ ts + ") Pressed 'W'")
        
    elif (cInput == "a"):
        keyboard.press("a")
        time.sleep(random.uniform(0, 5))
        keyboard.release("a")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'A'")
        print("\n("+ ts + ") Pressed 'A'")
        
    elif (cInput == "s"):
        keyboard.press("s")
        time.sleep(random.uniform(0, 5))
        keyboard.release("s")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'S'")
        print("\n("+ ts + ") Pressed 'S'")
        
    elif (cInput == "d"):
        keyboard.press("d")
        time.sleep(random.uniform(0, 5))
        keyboard.release("d")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'D'")
        print("\n("+ ts + ") Pressed 'D'")
        
    elif (cInput == "e"):
        keyboard.press("e")
        time.sleep(random.uniform(0, 5))
        keyboard.release("e")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'E'")
        print("\n("+ ts + ") Pressed 'E'") 
        
    elif (cInput == "space"):
        keyboard.press("space")
        time.sleep(random.uniform(0, 5))
        keyboard.release("space")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'SPACE'")
        print("\n("+ ts + ") Pressed 'SPACE'")
        
    elif (cInput == "right"):
        keyboard.press("right")
        time.sleep(random.uniform(0, 5))
        keyboard.release("right")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'RIGHT'")
        print("\n("+ ts + ") Pressed 'RIGHT'")
        
    elif (cInput == "left"):
        keyboard.press("left")
        time.sleep(random.uniform(0, 5))
        keyboard.release("left")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'LEFT'")
        print("\n("+ ts + ") Pressed 'LEFT'")
        
    elif (cInput == "lclick"):
        mouse.click()
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'LCLICK'")
        print("\n("+ ts + ") Pressed 'LCLICK'") 
        
    elif (cInput == "rclick"):
        mouse.right_click()
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'RCLICK'")
        print("\n("+ ts + ") Pressed 'RCLICK'")
        
    elif (cInput == "thi"):
        keyboard.press_and_release("/")
#        pyautogui.typewrite("Hi! I'm Jimmy, an artifical intelligence. I'm not very smart, but I can walk!")
        keyboard.press_and_release("enter")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'THI'")
        print("\n("+ ts + ") Pressed 'THI'") 
        
    elif (cInput == "thi"):
        keyboard.press_and_release("/")
#        pyautogui.typewrite("I'm not very smart.")
        keyboard.press_and_release("enter")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'THI'")
        print("\n("+ ts + ") Pressed 'THI'") 
        
    elif (cInput == "tffact"):
        keyboard.press_and_release("/")
#        pyautogui.typewrite("I have a strange obsession with repeating myself.")
        keyboard.press_and_release("enter")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'TFFACT'")
        print("\n("+ ts + ") Pressed 'TFFACT'")
        
    elif (cInput == "tthank"):
        keyboard.press_and_release("/")
#        pyautogui.typewrite("Thanks!")
        keyboard.press_and_release("enter")
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'TTHANK'")
        print("\n("+ ts + ") Pressed 'TTHANK'")
        
    elif (cInput == "ldrag"):
#        pyautogui.moveTo(random.uniform(0, x), random.uniform(0, y))
#        pyautogui.dragTo(random.uniform(0, x), random.uniform(0, y), button='left', duration=random.uniform(0, 5))
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'LDRAG'")
        print("\n("+ ts + ") Pressed 'LDRAG'") 
        
    elif (cInput == "rdrag"):
#        pyautogui.moveTo(random.uniform(0, x), random.uniform(0, y))
#        pyautogui.dragTo(random.uniform(0, x), random.uniform(0, y), button='right', duration=random.uniform(0, 5))
        ts = str(time.time())
        f.write("\n("+ ts + ") Pressed 'RDRAG'")
        print("\n("+ ts + ") Pressed 'RDRAG'")
        
    time.sleep(2.5)
