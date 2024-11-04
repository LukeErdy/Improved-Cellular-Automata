from CellularAutomata_model import *
from CellularAutomata_UI import *

def main():
	width = 80
	height = 70
	cell_size = 10
	color = 'blue'

	model = Model(width, height)
	root = Tk()
	ui = UI(model, root, cell_size, color)
	root.mainloop()

if __name__ == '__main__':
	main()