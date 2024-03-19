import keyboard, pyautogui, mouse, time, random, re
from thread import Thread
import requests

url = 'http://metaphorpsum.com/paragraphs/1/1'

def urlify(s):

	# Remove all non-word characters (everything except numbers and letters)
	s = re.sub(r"[^\w\s]", '', s)

	# Replace all runs of whitespace with a single dash
	s = re.sub(r"\s+", '-', s)

	return s

def jump():
    while True:
        should_jump = random.random() < 0.05  # 10% chance to jump
        if should_jump:
            keyboard.press("space")
            jump_duration = random.uniform(0.1, 5.0)  # Random duration between 0.1 and 5 seconds
            time.sleep(jump_duration)
            keyboard.release("space")
        time.sleep(2.5)  # Adjust the delay as needed
        
# Define a function for performing the actions with random chance and duration
def talk():
    while True:
        should_perform_actions = random.random() < 0.05  # 5% chance to perform the actions
        if should_perform_actions:
            time.sleep(0.5)
            keyboard.press_and_release('/')
            time.sleep(0.05)
            pyautogui.typewrite(requests.get(url).text)
            keyboard.press_and_release('enter')
        time.sleep(5)  # Adjust the delay as needed
        
jump_thread = Thread(target=jump)
jump_thread.start()
#talk_thread = Thread(target=talk)
#talk_thread.start()

pInputs = ["w", "a", "s", "d", "e", "left", "right", "lclick", "rclick", "ldrag", "rdrag"]#, "thi", "tthank", "tffact", "tnvsmart"]

x,y = pyautogui.size()
x,y=int(str(x)),int(str(y))

f = open(urlify(time.ctime(time.mktime(time.localtime()))) + ".txt", "w")

while True:
	cInput = random.choice(pInputs)

	match cInput:
		case "w":
			keyboard.press("w")
			time.sleep(random.uniform(.1, 5))
			keyboard.release("w")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'W'")
			print("\n("+ ts + ") Pressed 'W'")

		case "a":
			keyboard.press("a")
			time.sleep(random.uniform(.1, 5))
			keyboard.release("a")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'A'")
			print("\n("+ ts + ") Pressed 'A'")

		case "s":
			keyboard.press("s")
			time.sleep(random.uniform(.1, 5))
			keyboard.release("s")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'S'")
			print("\n("+ ts + ") Pressed 'S'")

		case "d":
			keyboard.press("d")
			time.sleep(random.uniform(.1, 5))
			keyboard.release("d")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'D'")
			print("\n("+ ts + ") Pressed 'D'")

		case "e":
			keyboard.press("e")
			time.sleep(random.uniform(.1, 5))
			keyboard.release("e")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'E'")
			print("\n("+ ts + ") Pressed 'E'")

		case "left":
			keyboard.press("left")
			time.sleep(random.uniform(1, 5))
			keyboard.release("left")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'LEFT'")
			print("\n("+ ts + ") Pressed 'LEFT'")
			
		case "right":
			keyboard.press("right")
			time.sleep(random.uniform(1, 5))
			keyboard.release("right")
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'RIGHT'")
			print("\n("+ ts + ") Pressed 'RIGHT'")
			
		case "lclick":
			mouse.click(button="left")
			ts = str(time.time())
			f.write("\n("+ ts + ") Clicked 'LEFT MOUSE BUTTON'")
			print("\n("+ ts + ") Clicked 'LEFT MOUSE BUTTON'")
		
		case "rclick":
			mouse.click(button="right")
			ts = str(time.time())
			f.write("\n("+ ts + ") Clicked 'RIGHT MOUSE BUTTON'")
			print("\n("+ ts + ") Clicked 'RIGHT MOUSE BUTTON'")
		
		case "ldrag":
			pyautogui.moveTo(random.uniform(0, x), random.uniform(0, y))
			pyautogui.dragTo(random.uniform(0, x), random.uniform(0, y), button='left', duration=random.uniform(0, 5))
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'LDRAG'")
			print("\n("+ ts + ") Pressed 'LDRAG'") 
		
		case "rdrag":
			pyautogui.moveTo(random.uniform(0, x), random.uniform(0, y))
			pyautogui.dragTo(random.uniform(0, x), random.uniform(0, y), button='right', duration=random.uniform(0, 5))
			ts = str(time.time())
			f.write("\n("+ ts + ") Pressed 'RDRAG'")
			print("\n("+ ts + ") Pressed 'RDRAG'")
		
	time.sleep(2.5)