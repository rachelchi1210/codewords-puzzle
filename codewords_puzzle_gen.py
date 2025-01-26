import random

def generate_codewords_puzzle(word_list, grid_size):
    # Create an empty grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def place_word(word):
        direction = random.choice(['H', 'V'])  # H for horizontal, V for vertical
        max_row = grid_size if direction == 'H' else grid_size - len(word)
        max_col = grid_size - len(word) if direction == 'H' else grid_size

        for _ in range(100):  # Try multiple positions
            row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
            positions = [(row, col + i) if direction == 'H' else (row + i, col) for i in range(len(word))]

            if all(grid[r][c] == ' ' for r, c in positions):
                for i, (r, c) in enumerate(positions):
                    grid[r][c] = word[i]
                return

    # Place each word on the grid
    for word in word_list:
        place_word(word.upper())

    letters = list(set(c for row in grid for c in row if c != ' '))
    letter_to_number = {letter: str(i + 1) for i, letter in enumerate(letters)}

    # Generate the coded puzzle grid
    coded_grid = [[letter_to_number.get(grid[r][c], '.') for c in range(grid_size)] for r in range(grid_size)]

    return coded_grid, grid
