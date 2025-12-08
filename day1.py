from data import Data
from termcolor import cprint

class Day1:
	def __init__(self):
		self.dial = [i for i in range(100)]
		self.input = 'day1/input'
		self.data = Data()
		self.data.load_data(self.input)
		self.part2()

	def part2(self):
		lines = self.data.get_raw()
		zeroes = 0
		currpos = 50
		for l in lines:
			val = int(l[1:])
			zeropasses = val // 100
			# if zeropasses > 0 :
				# cprint(f"passing 0 {zeropasses} times",'green')
			val = val % 100	
			if 'R' == l[0]:
				newpos = currpos + val
			if 'L' == l[0]:
				newpos = currpos - val
			cprint(f"provisionary newpos: {newpos}",'magenta')
			if newpos == 100 or newpos == 0:
				newpos = 0
				# cprint('passing 0','green')
				zeropasses += 1
			if newpos > 100:
				zeropasses += 1
				# cprint('passing 0','green')
				newpos = newpos % 100
			if newpos < 0:
				if currpos != 0:
					zeropasses += 1
				# cprint('passing 0','green')
				newpos = 100 + newpos
    
			cprint(f"{currpos} -> {newpos} ({zeropasses})",'cyan')
			currpos = newpos
			# cprint(currpos,'cyan')
			zeroes += zeropasses
		cprint(zeroes,'magenta')
				

	def part1(self):
		# print(dial)
		lines = self.data.get_raw()
		zeroes = 0
		currpos = 50
		for l in lines:
			val = int(l[1:])
			val = val % 100
			if 'R' == l[0]:
				# cprint(f"right {val}",'green')
				currpos += val
				currpos = currpos % 100
			if 'L' == l[0]:
				# cprint(f"left {val}",'green')
				currpos -= val
				currpos = self.dial[currpos]
			if 0 == currpos:
				zeroes += 1
		cprint(zeroes,'magenta')