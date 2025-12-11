from pathlib import Path
from termcolor import cprint
import pandas as pd
class Data:
	def __init__(self):
		self.raw = None
		self.my_dir = str(Path(__file__).parents[0])

	def load_data(self,fp,sep='\n'):
		fp = f"{self.my_dir}/{fp}"
		with open(fp,'r') as file:
			if '\n' == sep:
				self.raw = file.readlines()
				self.raw = [l.replace('\n','') for l in self.raw]
			else:
				data = file.read()
				self.raw = data.split(sep)

		return self.raw

	def duplicate_rows(self,d):
		if len(d) != len(list(set(d))):
			cprint("There are duplicate rows",'red')

	def load_multipart_data(self,fp):
		out = []
		fp = f"{self.my_dir}/{fp}"
		with open(fp,'r') as file:
			data = file.read()
			parts = data.split('\n\n')
			for p in parts:
				partlist = p.split('\n')
				partlist = [p.replace('\n','') for p in partlist]
				out.append(partlist)
		self.raw = out
		return self.raw

	def load_math_problems(self,fp):
		fp = f"{self.my_dir}/{fp}"
		lines = []
		with open(fp,'r') as file:
			lines = file.readlines()
		lines = [l.replace('\n','') for l in lines]
		self.raw = lines
		newlines = []
		for l in lines:
			while '  ' in l:
				l = l.replace('  ',' ')
			if l[0] == ' ':
				l = l[1:]
			if l[-1] == ' ':
				l = l[:-1]
			l = l.split(' ')
			newlines.append(l)
		lines = newlines
		# print(lines)
		self.df = pd.DataFrame(lines)
		return self.df

	def get_raw(self):
		return self.raw
	
	def get_df(self):
		return self.df