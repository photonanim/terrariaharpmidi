import json
#import mouse
import time
from time import sleep
#import pyautogui
from ahk import AHK
import sys
#import directkeys
#from pynput.mouse import Button, Controller
#import autoit
import win32api, win32con
#CreatedbyPhoton

ahk = AHK()
#mouse = Controller()

#pyautogui.FAILSAFE = False

#Loads .json into dictionary
with open('fuckmylife.json') as json_file: 
    data = json.load(json_file) 

h = 1440
w = 2560
x = 0
y = 0
#pulses per quarter note
tickrate = 480
#one beat in microseconds
tempo = 750000

#highest track
maxtrack = 0

track = 3


#Counter for.. counting the dictionary indicies
counter = 0
note_time = 0
section = 0
a = True
next_t = 0

times = {}


#Loads in time values with their keys as their counters
while counter < len(data):
	times[counter] = int(data[str(counter)][" 0"])
	counter += 1

counter = 0

#Click.
def click(x,y):
	#ahk.mouse_move(x=int(x), y=int(y), speed=0, blocking=True)
	#ahk.click(x,y)
	#mouse.position = (x, y)
	#autoit.mouse_click("left",int(x),int(y), speed=0)
	#win32api.SetCursorPos((int(x),int(y)))
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/w*65535.0), int(y/h*65535.0))
	#Clickity clicks the "z" key once.
	win32api.keybd_event(0x5A, 0, 0, 0)
	sleep(0.05)
	win32api.keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0)
	#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(x),int(y),0,0) 
	#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(x),int(y),0,0)

counter = 0

#Starting Track
track = 3

#Main, 1 = 1 because I'm too lazy to unindent all this shit.
if 1 == 1:
	note_time = 0

	######### Main sequence, find all the notes and waits.

	counter = 0
	true_counter = 0

	notes = []

	waits = []

	end_note = 0

	prev = 0

	while counter < len(data):
		if data[str(counter)][" Header"] == " Note_on_c" and int(data[str(counter)][" 1"])>= 48 and int(data[str(counter)][" 1"])<= 72:
			prev = note_time
			note_time = int(data[str(counter)][" 0"])
			#Finds time to next note in milliseconds
			wait = (((note_time-prev)/tickrate)*(tempo/1000))
			#Note! Always wait first from the waits list- that includes the first syncronization wait.
			note = int(data[str(counter)][" 1"])
			#Removes ghost notes from fucked up .midi source
			if note_time-prev > 50:
				waits.append(wait)
				notes.append(note)
			if data[str(counter-1)][" 1"] is not None and int(data[str(counter-1)][" 1"]) > end_note:
				end_note = int(data[str(counter-1)][" 0"])
		counter += 1

	print("It is starting.. now!")
	sleep(10)

	#Move the mouse and PLAY

	start_time = time.time()
	end_time =  start_time+((end_note/tickrate)*(tempo/1000000))

	if len(waits) > 0:
		next_t = start_time+(waits[0]/1000)

	counter = 0

	print(waits)

	#Clicker script
	if len(waits) > 0:
		while counter < len(waits):
			while time.time() < next_t:
				sleep(0.0001)
			starting_time = time.time()
			if counter < len(waits)-1:
				note = notes[counter]
				print(counter)
				next_t += (waits[counter]/1000)
			click(((note-48)*((1/48)*h))+w/2,h/2)
			#print("Playing: "+str(note))
			#print("Position: "+str(x) + ", " + str(y))
			print("Delay: " + str((time.time()-starting_time)*1000) + " milliseconds")
			print("Time to next note: " + str((next_t-time.time())*1000) + " milliseconds")
			counter += 1

# Total Ending
click(w,h)
print("Done.")
