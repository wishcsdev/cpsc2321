# Manager.py
import Pursuer
import Target

class manager:
	total_time_units = 0
	total_successful_interactions = 0
	total_failed_interactions = 0
	p = 0
	t = 0

	def __init__(self):
		return

	def main(self):
		print("The Tims\n")
		self.recursive_input_taker()
		
		print("Enter the turns to run simulation (1-100): ")
		timeunits = eval(input())
		
		# Set up behaviors in p and t
		self.p.behavior(timeunits)
		self.t.behavior(timeunits)
		plist = self.p.getList()
		tlist = self.t.getList()

		# Run simulation and print results.
		for i in range(0, timeunits):
			if plist[i] == tlist[i]:
				print('Turn # %d Match: Target %s, Pursuer %s' % (i, tlist[i], plist[i]))
				self.total_successful_interactions = self.total_successful_interactions + 1
			else:
				print('Turn # %d No Match: Target %s, Pursuer %s' % (i, tlist[i], plist[i]))
				self.total_failed_interactions = self.total_failed_interactions + 1
		
		print("END OF SIMULATION, FINAL RESULTS")
		self.p.report()
		self.t.report()
		print("\nOverall Statistics")
		print('No. Matches: %d No Mismatches: %d Total Attempts: %d' % (self.total_successful_interactions, self.total_failed_interactions, timeunits))
		proportion_of_matches = self.total_successful_interactions * 100 / timeunits
		proportion_of_mismatches = 100 - proportion_of_matches
		
		print('Proportion of Matches: %f percent, Proportion of Mismatches: %f percent' % (proportion_of_matches, proportion_of_mismatches))
		
		return

	def recursive_input_taker(self):
		if self.p == 0:
			print("Entering probabilities for the Pursure type of Tim. The sum of the two probabilities must equal 100%")
			print("Enter the X probabilty for pursuer without the % sign")
			x = eval(input())
			print("Enter the Y probability for pursuer without the % sign")
			y = eval(input())
			if ((x + y) != 100):
				print("Probabilities must sum to 100%. Try again\n")
				self.recursive_input_taker()
			else:
				self.p = Pursuer.pursuer(x,y)
			
		if self.t == 0:
			print("Entering probabilities for the Target type of Tim. The sum of hte two probabilities must equal 100%")
			print("Enter the X probabilty for target without the % sign")
			x = eval(input())
			print("Enter the Y probability for target without the % sign")
			y = eval(input())
			if ((x + y) != 100):
				print("Probabilities must equal to 100. Try again")
				self.recursive_input_taker()
			else:
				self.t = Target.target(x,y)
					
	
