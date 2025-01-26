import random

import random

import random

def load_words_from_file(filename="kids_combined_word_list.txt"):
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        return words
    except FileNotFoundError:
        return ["default", "words", "if", "file", "not", "found"]

def get_random_words(count):
    words = load_words_from_file()

    # Remove duplicates and empty words
    unique_words = list(set(filter(None, words)))

    # Return exactly 'count' number of words
    if len(unique_words) >= count:
        return random.sample(unique_words, count)
    else:
        return unique_words  # If not enough words, return all available

def generate_codewords_puzzle(word_list, grid_size):
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    solution_grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    letter_to_number = {}
    letter_count = 1

    # Limit the number of words to the chosen count
    selected_words = random.sample(word_list, min(len(word_list), grid_size))

    # Define possible placement directions (horizontal, vertical)
    directions = [(0, 1), (1, 0)]

    def can_place_word(word, row, col, direction):
        if direction == (0, 1):  # Horizontal
            if col + len(word) > grid_size:
                return False
            return all(grid[row][col + i] == '#' for i in range(len(word)))
        elif direction == (1, 0):  # Vertical
            if row + len(word) > grid_size:
                return False
            return all(grid[row + i][col] == '#' for i in range(len(word)))
        return False

    def place_word(word):
        nonlocal letter_count
        placed = False
        attempts = 0

        while not placed and attempts < 100:
            direction = random.choice(directions)
            row_start = random.randint(0, grid_size - 1)
            col_start = random.randint(0, grid_size - 1)

            if can_place_word(word, row_start, col_start, direction):
                for i, letter in enumerate(word):
                    if letter not in letter_to_number:
                        letter_to_number[letter] = letter_count
                        letter_count += 1

                    if direction == (0, 1):  # Horizontal
                        grid[row_start][col_start + i] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row_start][col_start + i] = letter

                    elif direction == (1, 0):  # Vertical
                        grid[row_start + i][col_start] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row_start + i][col_start] = letter

                placed = True

            attempts += 1

    # Place the selected words
    for word in selected_words:
        place_word(word.upper())

    return grid, solution_grid, letter_to_number

