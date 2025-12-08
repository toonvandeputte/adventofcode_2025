from data import Data
from termcolor import cprint

class Day2:
	def __init__(self):
		self.input = 'day2/input'
		self.data = Data()
		self.data.load_data(self.input,',')
		self.part2()

	def part1(self):
		ranges = self.data.get_raw()
		invalids = []
		for r in ranges:
			ids = r.split('-')
			start = int(ids[0])
			end = int(ids[1])
			idsinrange = sorted([i for i in range(start,end)] + [end])
			for id in idsinrange:
				sid = str(id)
				if len(sid) % 2 != 0:
					continue
				half = int(len(sid)/2)
				if sid[:half] == sid[half:]:
					invalids.append(id)
		cprint(sum(invalids),'green')

	def part2(self):
		ranges = self.data.get_raw()
		invalids = []
		for r in ranges:
			ids = r.split('-')
			start = int(ids[0])
			end = int(ids[1])
			idsinrange = sorted([i for i in range(start,end)] + [end])
			cprint(r,'cyan')
			for id in idsinrange:
				sid = str(id)
				if 1 == len(sid):
					continue
				if 1 == len(set(sid)):
					cprint(f"{id} is invalid",'red')
					invalids.append(id)
					continue
				if len(set(sid)) == len(sid):
					continue
				l = len(sid)
				for t in range(2, int(l//2) + 1):
					count = int(len(sid)/t)
					chunk = sid[:t]
					if sid == ''.join([chunk for i in range(count)]):
						cprint(f"{id} is invalid",'red')
						invalids.append(id)
						break
		invalids = list(set(invalids))
		cprint(sum(invalids),'green')