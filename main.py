import random
import numpy as np

############################################
sa, ri, ga, ma, pa, da, ni = range(7)
notesStr = ['sa', 'ri', 'ga', 'ma', 'pa', 'da', 'ni']

		#	sa ri ga ma pa da ni
transTable = np.matrix(
		[	[0.2, 0.5, 0.2, 0.0, 0.1, 0.0, 0.0],	# sa
			[0.3, 0.2, 0.3, 0.0, 0.2, 0.0, 0.0],	# ri
			[0.1, 0.3, 0.2, 0.0, 0.4, 0.0, 0.0],	# ga
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# ma
			[0.0, 0.2, 0.3, 0.0, 0.2, 0.0, 0.3],	# pa
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# da
			[0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.2]])	# ni

def nextNote(currentNote):
	pass

############################################

currentNote = int(random.uniform(0,8))
#currentState = [0 for i in range(8)]
currentState = np.zeros(7)
currentState[currentNote] = 1
print currentState
print currentState*transTable
'''
for count in range(20):
	print notesStr[currentNote] + '\t'
	currentNote = nextNote(currentNote)
'''
