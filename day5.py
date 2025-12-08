from data import Data
from termcolor import cprint
import copy

class Day5:
	def __init__(self):
		self.input = 2
		self.inputs = ['day5/testinput','day5/testinput2','day5/input']
		self.data = Data()
		self.data.load_multipart_data(self.inputs[self.input])
		self.part2()
		self.rangescache = []

	def get_data(self):
		raw = self.data.get_raw()
		return {
			'ranges' : raw[0],
			'ids' : raw[1]
		}

	def convert_ranges(self,ranges):
		out = []
		ranges = list(set(ranges))
		for r in ranges:
			limits = [int(v) for v in r.split('-')]
			if limits[0] > limits[1]:
				raise Exception("Malformed range")
			out.append([limits[0],limits[1]])
		return out

	def make_unique(self,ranges):
		hashable = [f"{r[0]}-{r[1]}" for r in ranges]
		uniq = list(set(hashable))
		return self.convert_ranges(uniq)

	def stringify_ranges(self,ranges):
		return [f"{r[0]}-{r[1]}" for r in ranges]

	def merge_ranges(self,range1,range2):

		if range2[0] <= range1[1]:
			return [[min([range1[0],range2[0]]), max([range1[1],range2[1]])]]
		return [range1,range2]

	def combine_ranges(self,ranges):
		cprint("in:",'green')
		print(ranges)
		out = []
		ranges.sort(key=lambda x:x[0])
		self.rangescache = copy.deepcopy(ranges)
		totalranges = len(ranges)
		for i in range(totalranges):
			next = i+1
			if next > totalranges-1:
				continue
			newranges = self.merge_ranges(ranges[i],ranges[next])
			out = out + newranges
			if len(newranges) == 1:
				cprint(f"Created a new range",'magenta')
				print(newranges[0])
				self.rangescache[i] = None
				self.rangescache[next] = None
				self.rangescache.append(newranges[0])
		self.rangescache = [r for r in self.rangescache if r != None]

		cprint("out:",'green')
		print(self.rangescache)
		return self.rangescache

	def collapse_ranges(self,ranges):
		total1 = len(ranges)
		cprint("first combine","yellow")
		newranges = self.combine_ranges(ranges)
		total2 = len(newranges)
		cprint(f"{total1} - {total2}",'green')
		while total1 != total2:
			total1 = total2
			newranges = self.combine_ranges(newranges)
			newranges = copy.deepcopy(newranges)
			total2 = len(newranges)
		return newranges

	def count_ids(self,ranges):
		out = 0
		for r in ranges:
			out += (r[1] - r[0] + 1)
		return out

	def id_is_fresh(self,id,ranges):
		for r in ranges:
			if id >= r[0] and id <= r[1]:
				return True
		return False

	def calc_minmax(self,ranges):
		ranges.sort(key=lambda x: x[0])
		min = ranges[0][0]
		max = ranges[-1][1]
		fullrange = max - min
		print(min,max,fullrange)

	def part1(self):
		expected_results = [3,529]
		d = self.get_data()

		ids = [int(id) for id in d['ids']]
		ranges = self.convert_ranges(d['ranges'])

		total = 0
		for id in ids:
			if self.id_is_fresh(id,ranges):
				total += 1

		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')

	def part2(self):
		expected_results = [14,14,344260049617193]
		d = self.get_data()
		self.data.duplicate_rows(d['ranges'])
		ranges = self.convert_ranges(d['ranges'])
		ranges.sort(key=lambda x: x[0])
		print(len(ranges))
		ranges = self.collapse_ranges(ranges)
		total = self.count_ids(ranges)
		print(len(ranges))
		ranges.sort(key=lambda x: x[0])
		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')
