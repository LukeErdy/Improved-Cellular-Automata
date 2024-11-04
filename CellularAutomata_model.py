class Model:

	def __init__(self, width, height):
		# Create grid according to dimensions
		self.grid = [[0] * width for y in range(height)]
		self.pats = ['111', '110', '101', '100', '011', '010', '001', '000']

	def edit(self, x, y):
		if x >= len(self.grid[0]) or x < 0 or y >= len(self.grid) or y < 0:
			print('Model.edit(self, x, y): coordinates (%d, %d) are invalid for %dx%d grid' % (x, y, len(self.grid[0]), len(self.grid)))
			return
		if self.grid[y][x] == 0: self.grid[y][x] = 1
		else: self.grid[y][x] = 0

	def run(self, rule_byte): # rule_byte is a string like '10011010'
		for y in range(len(self.grid) - 1):
			for x in range(len(self.grid[y])):
				if x - 1 < 0: pat = '0%d%d' % (self.grid[y][x], self.grid[y][x + 1])
				elif x + 1 == len(self.grid[y]): pat = '%d%d0' % (self.grid[y][x - 1], self.grid[y][x])
				else: pat = '%d%d%d' % (self.grid[y][x - 1], self.grid[y][x], self.grid[y][x + 1])
				self.grid[y + 1][x] = int(rule_byte[self.pats.index(pat)])
				
	def clear(self):
		for row in self.grid:
			for x in range(len(row)):
				row[x] = 0