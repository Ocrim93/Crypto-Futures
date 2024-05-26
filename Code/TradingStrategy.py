import math


class Future_Spot():
	def __init__(self, futures, spot):
		self.futures  =  futures
		self.spot = spot
		self.upper = 0.05
		self.lower = 0.03
		self.interest_rate = 
		self.time = 

	def long_signal(self):
		'''
			buy signal F < (Se^rT) 
		'''
		long_flag = False
		F = self.futures
		S = self.spot*math.exp(self.interest_rate*self*time)
		if (F-S) < 0 and abs(F-S/S) > self.lower:
			long_flag = True

		return long_flag

	def short_signal(self):
		short_flag = False
		F = self.futures
		S = self.spot*math.exp(self.interest_rate*self*time)
		if (F-S) > 0 and abs(F-S/S) > self.upper:
			short_flag = True

		return short_flag
			