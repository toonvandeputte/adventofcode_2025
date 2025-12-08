from data import Data
from termcolor import cprint

class Day3:
	def __init__(self):
		self.input = 'day3/input'
		self.data = Data()
		self.data.load_data(self.input,'\n')
		self.part2()

	def find_largest_nr(self,seq,digits=2):
		# cprint(seq,'yellow')
		number = ""
		startpos = 0

		count = list(reversed([i for i in range(digits)]))

		for c in count:
			searchseq= seq[startpos:len(seq)-c]
			# cprint(f"Searching in {searchseq} ({startpos}-{(len(seq)-c)})",'magenta')
			alldigits = list(searchseq)
			largest = max(alldigits)
			startpos = seq[startpos:].find(largest) + 1 + startpos
			number = f"{number}{largest}"

		return int(number)
		
	def part1(self):
		banks = self.data.get_raw()
		# print(banks)
		joltages = []
		for bank in banks:
			joltage = self.find_largest_nr(bank,2)
			cprint(f"{bank} -> {joltage}",'yellow')
			joltages.append(joltage)
		cprint(sum(joltages),'green')

	def part2(self):
		banks = self.data.get_raw()
		joltages = []
		for bank in banks:
			joltage = self.find_largest_nr(bank,12)
			cprint(f"{bank} -> {joltage}",'yellow')
			joltages.append(joltage)
		cprint(sum(joltages),'green')
		