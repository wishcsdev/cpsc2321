# Pursuer.py
from random import shuffle

class pursuer:
	pursuer_x_count = 0
	pursuer_y_count = 0
	prob_x_int = 0
	prob_y_int = 0
	rand_list = []
	x_behavior = 'x'
	y_behavior = 'y'

	# Initializer for the module.
	def __init__(self, probx, proby):
		# Save the probabilities for the target from the main application.
		self.prob_x_int = probx
		self.prob_y_int = proby

	# Determine the behavior that will occur during the interaction and determine the random numbers.
	def behavior(self, timeunits):
		# Use the timeunits to determine the random list for the target.
		x_behavior_count = int((self.prob_x_int * timeunits) / 100)
		y_behavior_count = int(timeunits - x_behavior_count)
		self.pursuer_x_count = x_behavior_count
		self.pursuer_y_count = y_behavior_count

		# Load x values
		for i in range(0, x_behavior_count):
			self.rand_list.append(self.x_behavior)

		# Load y values
		for j in range(x_behavior_count, timeunits):
			self.rand_list.append(self.y_behavior)

		# Randomize list
		shuffle(self.rand_list)
		return
		
	def getList(self):
		return self.rand_list
		
	def report(self):
		print("Pursuer Statistics")
		print('Number of Xs: %d, Number of Ys: %d' % (self.pursuer_x_count, self.pursuer_y_count))
		return
	
