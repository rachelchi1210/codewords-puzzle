import random

def generate_codewords_puzzle(words, grid_size):
    # Initialize empty grid with black squares
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    solution_grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    placed_words = []

    def place_word(word):
    max_row = len(grid)
    max_col = len(grid[0])

    for _ in range(100):  # Attempt multiple placements
        r, c = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
        direction = random.choice([(0, 1), (1, 0)])  # Right or down
        
        # Check if word fits in the chosen direction
        if direction == (0, 1) and c + len(word) <= max_col:
            if all(grid[r][c + i] == '#' for i in range(len(word))):
                for i in range(len(word)):
                    grid[r][c + i] = word[i]
                return True
        
        elif direction == (1, 0) and r + len(word) <= max_row:
            if all(grid[r + i][c] == '#' for i in range(len(word))):
                for i in range(len(word)):
                    grid[r + i][c] = word[i]
                return True

    return False  # Word placement failed


            # Check if the word fits without conflict
            conflict = False
            for i in range(len(word)):
                r, c = row + i * dir_x, col + i * dir_y
                if grid[r][c] != '#':
                    conflict = True
                    break

            if not conflict:
                for i in range(len(word)):
                    r, c = row + i * dir_x, col + i * dir_y
                    grid[r][c] = word[i]
                    solution_grid[r][c] = word[i]
                placed_words.append(word)
                return True
        return False

    for word in words:
        if not place_word(word.upper()):
            continue  # Skip if the word can't be placed

    # Assign numbers to letters
    letter_to_number = {}
    counter = 1
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] != '#':
                letter = grid[row][col]
                if letter not in letter_to_number:
                    letter_to_number[letter] = counter
                    counter += 1
                grid[row][col] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                solution_grid[row][col] = f"{letter}<sup>{letter_to_number[letter]}</sup>"

    return grid, solution_grid, letter_to_number, placed_words
