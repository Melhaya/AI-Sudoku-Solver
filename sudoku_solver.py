from utils import *
from collections import defaultdict


def grid_values(grid):
	"""Convert grid string into {<box>: <value>} dict with '.' value for empties.

	Args:
		grid: Sudoku grid in string form, 81 characters long
	Returns:
		Sudoku grid in dictionary form:
		- keys: Box labels, e.g. 'A1'
		- values: Value in corresponding box, e.g. '8', or '.' if it is empty.
	"""
	assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
	#sudoku_grid = dict(zip(boxes, grid))
	sudoku_grid = dict()
	for i, value in enumerate(grid):
		if value != '.':
			sudoku_grid[boxes[i]]=value
		else:
			sudoku_grid[boxes[i]]=cols

	
	return sudoku_grid

def eliminate(sudoku_grid):
	"""Eliminate values from peers of each box with a single value.

	Go through all the boxes, and whenever there is a box with a single value,
	eliminate this value from the set of values of all its peers.

	Args:
		sudoku_grid: Sudoku in dictionary form.
	Returns:
		Resulting Sudoku in dictionary form after eliminating values.
	"""
	
	for key, value in sudoku_grid.items():
		if len(value) == 1:
			for peer in peers[key]:
				sudoku_grid[peer]=sudoku_grid[peer].replace(value, '')
	return sudoku_grid

def only_choice(sudoku_grid):
	"""Finalize all values that are the only choice for a unit.

	Go through all the units, and whenever there is a unit with a value
	that only fits in one box, assign the value to this box.

	Input: Sudoku in dictionary form.
	Output: Resulting Sudoku in dictionary form after filling in only choices.
	"""
	for square_unit in square_units:
		for digit in '123456789':
			number_locations = []
			for box in square_unit:
				if digit in sudoku_grid[box]:
					number_locations.append(box)
			if len(number_locations) == 1:
				sudoku_grid[number_locations[0]] = digit
	return sudoku_grid

def reduce_puzzle(values):
	stalled = False
	while not stalled:
		# Check how many boxes have a determined value
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

		# Use the Eliminate Strategy
		values = eliminate(values)
		# Use the Only Choice Strategy
		values = only_choice(values)

		# Check how many boxes have a determined value, to compare
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
		# If no new values were added, stop the loop.
		stalled = solved_values_before == solved_values_after
		# Sanity check, return False if there is a box with zero available values:
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values

def search(values):
	'''Using depth-first search and propagation, create a search 
	tree and solve the sudoku."
	'''
	# First, reduce the puzzle using the reduce_puzzle function
	sudoku_grid = reduce_puzzle(values)
	if sudoku_grid is False:
		return False ## Failed earlier
	
	# If sudoku is solved, return the solution
	if all(len(sudoku_grid[box]) == 1 for box in boxes): 
		return sudoku_grid

	# Choose one of the unfilled squares with the fewest possibilities
	#for box in sudoku_grid.keys()
	minvalue = 9
	for box in boxes:
		if len(sudoku_grid[box]) > 1:
			if len(sudoku_grid[box]) < minvalue:
				minvalue = len(sudoku_grid[box])
				bestbox = box
	
	# Now use recursion to solve each one of the resulting sudokus,
	#and if one returns a value (not False), return that answer!
	for value in sudoku_grid[bestbox]:
		new_sudoku = sudoku_grid.copy()
		new_sudoku[bestbox] = value
		attempt = search(new_sudoku)
		if attempt:
			return attempt

easy_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
hard_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

sudoku_grid = grid_values(hard_grid)
display(sudoku_grid)
print("############################################################################################")
sudoku_grid = search(sudoku_grid)
if sudoku_grid != False:	
	display(sudoku_grid)
else:
	print("Grid Not Solvable")
