from tkinter import *

class UI:

	def __init__(self, model, root, cell_size, color):
		self.color = color
		self.model = model
		root.title('Cellular Automata')
		self.root = root
		self.cell_size = cell_size
		self.canvas = Canvas(root, height = model.height * cell_size, width = model.width * cell_size)
		frame = Frame(root)
		frame.grid(row = 0, column = 0)
		self.canvas.grid(row = 1, column = 0)
		self.cells = []

		for row in range(model.height * cell_size):
			if row % cell_size == 0:
				cell_row = []
				for column in range(model.width * cell_size):
					if column % cell_size == 0:
						cell_row.append(self.canvas.create_rectangle(column, row, column + cell_size, row + cell_size, fill = 'white'))
				self.cells.append(cell_row)

		self.run_btn = Button(frame, text = 'Run', bg = '#CCCCCC', command = self.run)
		self.run_btn.pack(side = LEFT)
		self.canvas.bind('<Button-1>', self.edit)
		self.clear_btn = Button(frame, text = 'Clear', bg = '#CCCCCC', command = self.clear)
		self.clear_btn.pack(side = LEFT)
		quit_btn = Button(frame, text = 'Quit', bg = '#CCCCCC', command = self.quit)
		quit_btn.pack(side = LEFT)

	def run(self):
		self.clear_btn.config(state = DISABLED)
		self.run_btn.config(text = 'Running...', state = DISABLED)
		self.model.run('00011110', self)
		self.run_btn.config(text = 'Run', state = NORMAL)
		self.clear_btn.config(state = NORMAL)

	def edit(self, event):
		row = int(event.y / self.cell_size)
		column = int(event.x / self.cell_size)
		self.model.edit(column, row, self)

	def clear(self):
		self.run_btn.config(state = DISABLED)
		self.clear_btn.config(text = 'Clearing...', state = DISABLED)
		self.model.clear(self)
		self.clear_btn.config(text = 'Clear', state = NORMAL)
		self.run_btn.config(state = NORMAL)

	def quit(self):
		self.root.destroy()