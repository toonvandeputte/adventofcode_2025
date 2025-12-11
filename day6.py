from data import Data
from termcolor import cprint
import math
import pandas as pd

class Day6:
	def __init__(self):
		self.input = 1
		self.inputs = ['day6/testinput','day6/input']
		self.data = Data()
		self.data.load_math_problems(self.inputs[self.input])
		self.part2()

	def part1(self):
		expected_results = [4277556,4722948564882]
		df = self.data.get_df()
		cols = df.columns
		total = 0
		for c in cols:
			params = list(df[c])
			r = self.calc_col_part1(params)
			print(params)
			print(r)
			total += r
		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')

		# print(df)

	def part2(self):
		expected_results = [3263827,9581313737063]
		lines = self.data.get_raw()
		numberpositions = []
		allpositions = []
		for l in lines:
			for i,c in enumerate(l):
				if i not in allpositions:
					allpositions.append(i)
				if c != ' ' and i not in numberpositions:
					numberpositions.append(i)
		spacepositions = [i for i in allpositions if i not in numberpositions]
		print(lines)
		print(spacepositions)
		cols = {}
		for l in lines:
			# cprint("line",'green')
			prevpos = -1
			col = 0
			for s in spacepositions:
				colval = l[prevpos+1:s]
				if col not in cols:
					cols[col] = []
				cols[col].append(colval)
				prevpos = s
				col+=1
			if col not in cols:
				cols[col] = []
			colval = l[s+1:]
			cols[col].append(colval)
		print(list(cols.values()))
		df = pd.DataFrame(list(cols.values()))
		df = df.transpose()
		print(df)
		total = 0
		for c in df.columns:
			total += self.calc_col_part2(list(df[c]))
		if total == expected_results[self.input]:
			cprint(total,'green')
		else:
			cprint(total,'red')

	def calc_col_part2(self,col:list):
		n_numbers = len(col[0])
		# print(n_numbers)
		numbers = {}
		operand = col[-1].strip()
		for i in range(n_numbers,0,-1):
			numbers[i] = ''
			# print(f"subcol {(i)}")
			for val in col[:-1]:
				char = val[i-1]
				if char != ' ':
					numbers[i] = f"{numbers[i]}{char}"
		figures = list(numbers.values())
		figures = [int(f) for f in figures]
		if '+' == operand:
			result = sum(figures)
		if '*' == operand:
			result = math.prod(figures)
		return result

	def calc_col_part1(self,col:list):
		operand = col[-1]
		figures = [int(v) for v in col[:-1]]
		print(figures)
		print(operand)
		if '+' == operand:
			result = sum(figures)
		if '*' == operand:
			result = math.prod(figures)
		return result