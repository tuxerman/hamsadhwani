import random
import numpy as np

############################################
sa, ri, ga, ma, pa, da, ni = range(7)
notesStr = ['sa', 'ri', 'ga', 'ma', 'pa', 'da', 'ni']


		#	sa ri ga ma pa da ni
transTable = np.matrix([
			[0.1, 0.5, 0.3, 0.0, 0.1, 0.0, 0.0],	# sa
			[0.2, 0.1, 0.5, 0.0, 0.2, 0.0, 0.0],	# ri
			[0.1, 0.3, 0.1, 0.0, 0.5, 0.0, 0.0],	# ga
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# ma
			[0.0, 0.2, 0.2, 0.0, 0.1, 0.0, 0.5],	# pa
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# da
			[0.3, 0.0, 0.0, 0.0, 0.5, 0.0, 0.2]])	# ni

'''
transTable = np.matrix([
			# sa  ri   ga   ma   pa   da   ni
			[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# sa
			[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],	# ri
			[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],	# ga
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# ma
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],	# pa
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],	# da
			[0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5]])	# ni
'''

##############################################
#currentNote = int(random.uniform(0,8))
currentNote = 0
print currentNote
#currentState = [0 for i in range(8)]
for loop in range(20):
	currentState = np.zeros(7)
	currentState[currentNote] = 1
	#print 'Current state', notesStr[currentNote]
	nextState = (currentState*transTable).tolist()[0]
	#print 'Next state probabilities', nextState

	## pick one based on weights
	cumProb = 0
	rnd = random.uniform(0,1)
	#print 'Random number', rnd

	for	i in range(8):
		cumProb += nextState[i]
		#print 'cumProb',cumProb
		if rnd < cumProb:
			print 'Next note is', notesStr[i]
			currentNote = i
			break

