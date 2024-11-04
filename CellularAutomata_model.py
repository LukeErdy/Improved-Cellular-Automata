import numpy as np

class Model:

	def __init__(self, width, height):
		# Create grid according to dimensions
		self.grid = [[0] * width for y in range(height)]
		self.pats = ['111', '110', '101', '100', '011', '010', '001', '000']
		self.width = width
		self.height = height

	def edit(self, x, y, ui):
		if x >= len(self.grid[0]) or x < 0 or y >= len(self.grid) or y < 0:
			print('Model.edit(self, x, y): coordinates (%d, %d) are invalid for %dx%d grid' % (x, y, len(self.grid[0]), len(self.grid)))
			return
		if self.grid[y][x] == 0:
			self.grid[y][x] = 1
			ui.canvas.itemconfig(ui.cells[y][x], fill = ui.color)
		else:
			self.grid[y][x] = 0
			ui.canvas.itemconfig(ui.cells[y][x], fill = 'white')

	def run(self, rule_byte, ui): # rule_byte is a string like '10011010'
		for y in range(len(self.grid) - 1):
			for x in range(len(self.grid[y])):
				if x - 1 < 0: pat = '%d%d%d' % (self.grid[y][-1], self.grid[y][x], self.grid[y][x + 1])
				elif x + 1 == len(self.grid[y]): pat = '%d%d%d' % (self.grid[y][x - 1], self.grid[y][x], self.grid[y][0])
				else: pat = '%d%d%d' % (self.grid[y][x - 1], self.grid[y][x], self.grid[y][x + 1])
				self.grid[y + 1][x] = int(rule_byte[self.pats.index(pat)])
				if self.grid[y + 1][x] == 1: ui.canvas.itemconfig(ui.cells[y + 1][x], fill = ui.color)
				elif self.grid[y + 1][x] == 0: ui.canvas.itemconfig(ui.cells[y + 1][x], fill = 'white')
			ui.canvas.update()

	def game_of_life(self, ui):
		while True:
			neighbors = (
				np.roll(np.roll(self.grid, 1, 0), 1, 1) +
				np.roll(self.grid, 1, 0) +
				np.roll(np.roll(self.grid, 1, 0), -1, 1) +
				np.roll(self.grid, 1, 1) +
				np.roll(self.grid, -1, 1) +
				np.roll(np.roll(self.grid, -1, 0), 1, 1) +
				np.roll(self.grid, -1, 0) +
				np.roll(np.roll(self.grid, -1, 0), -1, 1)
			)
			self.grid = (neighbors == 3) | ((self.grid == 1) & (neighbors == 2))
			self.grid = self.grid.astype(int)
			for y in range(len(self.grid)):
				for x in range(len(self.grid[y])):
					if self.grid[y][x] == 0: ui.canvas.itemconfig(ui.cells[y][x], fill = 'white')
					else: ui.canvas.itemconfig(ui.cells[y][x], fill = ui.color)
			ui.canvas.update()
					
				
	def clear(self, ui):
		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				self.grid[y][x] = 0
				ui.canvas.itemconfig(ui.cells[y][x], fill = 'white')
			ui.canvas.update()