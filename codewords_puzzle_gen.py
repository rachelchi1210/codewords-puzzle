import random

def generate_codewords_puzzle(word_list, grid_size):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def place_word(word):
        if len(word) > grid_size:
            return False  # Skip words that are too long to fit

        directions = ['H', 'V']
        random.shuffle(directions)

        for direction in directions:
            max_row = grid_size if direction == 'H' else grid_size - len(word)
            max_col = grid_size - len(word) if direction == 'H' else grid_size

            if max_row <= 0 or max_col <= 0:
                continue

            for _ in range(100):  # Attempt placement up to 100 times
                row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
                positions = [(row, col + i) if direction == 'H' else (row + i, col) for i in range(len(word))]

                if all(grid[r][c] == ' ' for r, c in positions):
                    for i, (r, c) in enumerate(positions):
                        grid[r][c] = word[i]
                    return True
        return False

    # Sort words by length (longest first to avoid blocking space for smaller words)
    word_list.sort(key=len, reverse=True)
    
    placed_words = [word for word in word_list if place_word(word.upper())]

    # Assign numbers to letters
    letters = sorted(set(c for row in grid for c in row if c != ' '))
    letter_to_number = {letter: str(index + 1) for index, letter in enumerate(letters)}

    # Create coded grid with numbers and letters in each cell
    coded_grid = [[f"{grid[r][c]}<sup>{letter_to_number.get(grid[r][c], '')}</sup>" if grid[r][c] != ' ' else '#' for c in range(grid_size)] for r in range(grid_size)]

    return coded_grid, grid, letter_to_number, placed_words

