import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def place_word(word):
        direction = random.choice(['H', 'V'])
        max_row = grid_size if direction == 'H' else grid_size - len(word)
        max_col = grid_size - len(word) if direction == 'H' else grid_size

        for _ in range(100):  # Attempt multiple placements
            row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
            positions = [(row, col + i) if direction == 'H' else (row + i, col) for i in range(len(word))]

            if all(grid[r][c] == ' ' for r, c in positions):
                for i, (r, c) in enumerate(positions):
                    grid[r][c] = word[i]
                return True
        return False

    # Place words in the grid
    for word in word_list:
        place_word(word.upper())

    # Assign random numbers to letters
    letters = list(set(c for row in grid for c in row if c != ' '))
    letter_to_number = {letter: str(i + 1) for i, letter in enumerate(letters)}

    # Create coded grid with numbers
    coded_grid = [[letter_to_number.get(grid[r][c], random.choice(string.digits)) if grid[r][c] != ' ' else '■' for c in range(grid_size)] for r in range(grid_size)]

    return coded_grid, grid

