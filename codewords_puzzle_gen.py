import random

def generate_codewords_puzzle(word_list, grid_size):
    # Initialize the grid with empty spaces
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    solution_grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    
    placed_words = []
    letter_to_number = {}
    current_number = 1

    def can_place_word(word, row, col, direction):
        """ Check if the word can be placed at the given position and direction. """
        if direction == 'H':
            if col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row][col + i] != '#' and grid[row][col + i] != word[i]:
                    return False
        else:  # Vertical placement
            if row + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col] != '#' and grid[row + i][col] != word[i]:
                    return False
        return True

    def place_word(word):
        """ Place the word in a random position and direction if possible. """
        nonlocal current_number
        for _ in range(100):  # Try 100 times to place the word
            direction = random.choice(['H', 'V'])
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)

            if can_place_word(word, row, col, direction):
                for i in range(len(word)):
                    if direction == 'H':
                        grid[row][col + i] = word[i]
                        solution_grid[row][col + i] = f"{word[i]}<sup>{current_number}</sup>"
                    else:
                        grid[row + i][col] = word[i]
                        solution_grid[row + i][col] = f"{word[i]}<sup>{current_number}</sup>"
                    
                    # Assign a unique number to each letter
                    if word[i] not in letter_to_number:
                        letter_to_number[word[i]] = current_number
                        current_number += 1
                
                placed_words.append(word)
                return True
        return False

    # Shuffle the word list to ensure random placement
    random.shuffle(word_list)

    # Try to place each word
    for word in word_list:
        if not place_word(word.upper()):
            continue  # Skip the word if it cannot be placed

    # Replace letters with their corresponding numbers in the coded grid
    coded_grid = [[str(letter_to_number[c]) if c in letter_to_number else '#' for c in row] for row in grid]

    return coded_grid, solution_grid, letter_to_number, placed_words
