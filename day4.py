from data import Data
from termcolor import cprint

class Day4:
	def __init__(self):
		self.input = 1
		self.inputs = ['day4/testinput','day4/input']
		self.data = Data()
		self.data.load_data(self.inputs[self.input],'\n')
		self.part2()
  
	def count_accessible_rolls(self,grid):
		acc = self.fetch_accessible_rolls(grid)
		return len(acc)

	def fetch_accessible_rolls(self,grid):
		accessibles = []
		for row,rowval in enumerate(grid):
			for col,colval in enumerate(rowval):
				acc = self.accessible(grid,row,col)
				if True == acc:
					accessibles.append([row,col])
					# cprint(f"{row},{col} is accessible",'green')
					# total += 1
				# adjacents = self.get_adjacents(grid,row,col)
				# cprint(f"{row},{col} has adjacents:",'yellow')
				# print(adjacents)
				# for a in adjacents:
				# 	aval = grid[a[0]][a[1]]
				# 	cprint(f"{a[0]},{a[1]}: {aval}",'cyan')
		return accessibles

	def print_grid(self,grid):
		out = ""
		for r,rval in enumerate(grid):
			rowstr = ""
			for c,cval in enumerate(rval):
				rowstr = f"{rowstr}{cval}"
			out = f"{out}{rowstr}\n"
		print(out)

	def accessible(self,grid,row,col,maxrolls=3):
		rolls = 0
		maxrow = len(grid) - 1
		maxcol = len(grid[0]) - 1
		# adjacents = []
		if grid[row][col] != "@":
			return False
		for rshift in range(-1,2):
			for cshift in range(-1,2):
				r = (row + rshift)
				# print(f"{row} -> {r}")
				if r < 0 or r > maxrow:
					continue
				c = (col + cshift)
				if c < 0 or c > maxcol:
					continue
				if r == row and c == col:
					continue
				# adjacents.append([r,c])
				if "@" == grid[r][c]:
					rolls += 1
					if rolls > maxrolls:
						return False
		return True
		# return adjacents

	def remove_rolls(self,grid,positions):
		cprint(f"remove {len(positions)} positions", 'cyan')
		for p in positions:
			# cprint(f"{p[0]},{p[1]} -> {grid[p[0]][p[1]]}", 'yellow')
			row = list(grid[p[0]])
			row[p[1]] = '.'
			grid[p[0]] = ''.join(row)
		# self.print_grid(grid)
		return grid

	def part1(self):
		expected_results = [13,1495]
		grid = self.data.get_raw()
		# print(grid)
		total = self.count_accessible_rolls(grid)
		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')

	def part2(self):
		expected_results = [43,8768]
		removed = 0
		grid = self.data.get_raw()
		# self.print_grid(grid)
		# return True
		acc = self.fetch_accessible_rolls(grid)
		# grid = self.remove_rolls(grid,acc)
		# acc = self.fetch_accessible_rolls(grid)
		# grid = self.remove_rolls(grid,acc)
		# return True
		while len(acc) > 0:
			# print(len(acc))
			removed += len(acc)
			grid = self.remove_rolls(grid,acc)
			acc = self.fetch_accessible_rolls(grid)
		if removed == expected_results[self.input]:
			cprint(removed,'green')
		else:
			cprint(removed,'red')

		