import sys
import plotly
import plotly.graph_objs as go 
import re
import math


data = open("piano.csv", "r")
lines = data.readlines()

key = []
notes = []

count = []
for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",") # [make, model, year]
	key.append(info[0])
	notes.append(info[1])

def piano(list):
	print "Play a song"
	print "Hit m to quit"
	# keyboard = raw_input("> ")
	keyboard = ""
	while 1==1:
		# found = false
		# for i in range(0, len(key)):
		# 	if keyboard == key[i]:
		# 		print notes[i] 
		# 		found = true
		# if not found:
		# 	print "Try another key"
		# else:
		# 	piano()
		keyboard = raw_input("> ")
		if keyboard in key:
			print notes[key.index(keyboard)]
		elif keyboard == "m":
			#stops loop, leave while statment
			break
		else:
			print "Try another key"
		
	print "Quitting"
