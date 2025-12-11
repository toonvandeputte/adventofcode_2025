from data import Data
from termcolor import cprint
import math
import pandas as pd

class Day7:
	def __init__(self):
		self.input = 0
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
		self.split_positions = []
		start = self.find_startpos()
		# tree = []
		# next = self.expand_pos(start)
		# tree = tree + next
		# for n in next:
		# 	print(n)
		# 	tree = tree + self.expand_pos(n)
		print(f"part1 starting from ({start[0]},{start[1]})")
		# exit()
		first = self.project_beam(start)
		splits = self.expand_pos(first)
		print(splits)
		# print(splits)
		# print(len(splits))
		split_positions = [self.intify_pos(p) for p in self.split_positions]
		treemap = self.update_grid(self.grid,split_positions)
		print(len(self.split_positions))
		self.print_grid(treemap)

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

	def is_visited(self,pos):
		posstr = self.stringify_pos(pos)
		if posstr in self.split_positions:
			return True
		return False

	def project_beam(self,startpos):
		startline = startpos[0] + 1
		# print(f"startline from ({startpos[0]},{startpos[1]}): {startline}")
		for i,r in enumerate(self.grid[startline:]):
			# xpos = r.find('^')
			if r[startpos[1]] == '^':
			# 	xpos = 
			# if xpos >= 0:
				out = [i+startline,startpos[1]]
				outstr = self.stringify_pos(out)
				if outstr not in self.split_positions:
					self.split_positions.append(outstr)
				return out

	def make_unique(self,tree):
		strtree = [self.stringify_pos(pos) for pos in tree]
		strtree = list(set(strtree))
		strtree.sort()
		out = []
		# print(strtree)
		for s in strtree:
			pos = self.intify_pos(s)
			out.append(pos)

		return out

	def build_tree(self,positions):
		# tree = positions
		# tree = self.expand_pos(pos)
		tree = positions
		for p in positions:
			next = self.expand_pos(p)
			if next:
				tree = tree + next + self.build_tree(next)
		return self.make_unique(tree)
		
		# print(newpos)
		# exit()
		# if newpos:
		# 	for n in newpos:
		# 		self.expand_pos(n)
				# print(f"add ({n[0]},{n[1]}) to tree")
				# tree.append(n)
				# # print(tree)
				# # exit()
				# tree = self.make_unique(tree)
				# tree = tree + self.build_tree(n)

		# tree = [pos] + self.expand_pos(pos)
		# return tree
		# return self.make_unique(tree)
		# newpos = self.expand_pos(pos)
		# print(newpos)
		# while newpos:
		# 	for p in newpos:
		# 		tree = tree + self.build_tree(p)
		# return tree

	def expand_pos(self,pos):
		startpositions = self.nextbeams(pos)
		print(startpositions)
		out = []
		for p in startpositions:
			split = self.project_beam(pos)
			print(split)
			if split:
				out.append(split)
		out = self.make_unique(out)
		cprint(f"{pos[0]},{pos[1]} ->",'green')
		for o in out:
			cprint(f"   {o[0]},{o[1]}",'green')
		return out
		

	def nextbeams(self,pos):
		# print(pos)
		leftx = pos[1] - 1
		rightx = pos[1] + 1
		out = []
		if leftx >= 0:
			out.append([pos[0],leftx])
		if rightx < len(self.grid[0]):
			out.append([pos[0],rightx])
		# print(out)
		# exit()
		return out