from data import Data
from termcolor import cprint
import math
import pandas as pd

class Day7:
	def __init__(self):
		self.input = 1
		self.inputs = ['day7/testinput','day7/input']
		self.data = Data()
		self.data.load_data(self.inputs[self.input])
		self.grid = self.data.get_raw()
		self.part1()
	
	def update_grid(self,grid,positions,symbol = 'X'):
		grid = grid.copy()
		for p in positions:
			gridline = list(grid[p[0]])
			gridline[p[1]] = 'X'
			grid[p[0]] = ''.join(gridline)
		return grid

	def print_grid(self,grid):
		screen = '\n'.join(grid)
		print(screen)

	def part1(self):
		expected_results = [21,1504]
		# self.split_positions = []
		start = self.find_startpos()
		print(f"part1 starting from ({start[0]},{start[1]})")

		first = self.project_beam(start)
		positions = self.build_tree(first)

		positions = [self.intify_pos(p) for p in positions]
		treemap = self.update_grid(self.grid,positions)
		# print(split_positions)
		print(positions)
		total = len(positions)
		self.print_grid(self.grid)
		self.print_grid(treemap)
		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')

	def find_startpos(self):
		for i,r in enumerate(self.grid):
			for j,c in enumerate(r):
				if 'S' == c:
					return [i,j]

	def stringify_pos(self,pos):
		return f"{pos[0]}-{pos[1]}"

	def intify_pos(self,pos):
		p = pos.split("-")
		return [int(c) for c in p]

	def project_beam(self,startpos):
		# cprint(len(self.split_positions),'green')
		startline = startpos[0] + 1
		for i,r in enumerate(self.grid[startline:]):
			# xpos = r.find('^')
			if r[startpos[1]] == '^':
			# 	xpos = 
			# if xpos >= 0:
				out = [i+startline,startpos[1]]
				outstr = self.stringify_pos(out)
				# if outstr not in self.split_positions:
				# self.split_positions.append(outstr)
				return out

	def make_unique(self,tree):
		strtree = [self.stringify_pos(pos) for pos in tree]
		strtree = list(set(strtree))
		strtree.sort()
		out = []
		for s in strtree:
			pos = self.intify_pos(s)
			out.append(pos)

		return out

	def build_tree(self,first):
		# first = self.project_beam(startpos)
		firststr = self.stringify_pos(first)
		to_expand = [firststr]
		found = [firststr]
		while to_expand:
			cprint(f"{len(to_expand)} / {len(found)}", 'green')
			pos = to_expand.pop()
			pos = self.intify_pos(pos)
			next = self.expand_pos(pos)
			for n in next:
				strn = self.stringify_pos(n)
				if strn not in to_expand and strn not in found:
					to_expand.append(strn)
				if strn not in found:
					found.append(strn)
		return found
			

	def build_tree_old(self,positions):
		# tree = positions
		# tree = self.expand_pos(pos)
		tree = positions
		for p in positions:
			next = self.expand_pos(p)
			if next:
				tree = tree + next + self.build_tree(next)
		# cprint(len(tree),'green')
		return self.make_unique(tree)

	def expand_pos(self,pos):
		startpositions = self.nextbeams(pos)
		out = []
		for p in startpositions:
			split = self.project_beam(p)
			if split:
				out.append(split)
		# out = self.make_unique(out)
		return out
		

	def nextbeams(self,pos):
		leftx = pos[1] - 1
		rightx = pos[1] + 1
		out = []
		if leftx >= 0:
			out.append([pos[0],leftx])
		if rightx < len(self.grid[0]):
			out.append([pos[0],rightx])
		return out