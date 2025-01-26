import random

# Load words from a file
def load_words_from_file(filename="kids_combined_word_list.txt"):
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        return words
    except FileNotFoundError:
        return ["default", "words", "if", "file", "not", "found"]

# Get random words from the loaded list
def get_random_words(count):
    words = load_words_from_file()
    return random.sample(words, min(count, len(words)))

# Generate codewords puzzle with a strict word limit
def generate_codewords_puzzle(word_list, grid_size):
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    solution_grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    letter_to_number = {}
    letter_count = 1

    # Select only the requested number of words
    selected_words = word_list[:grid_size] if len(word_list) > grid_size else word_list

    # Define possible placement directions (horizontal, vertical)
    directions = [(0, 1), (1, 0)]  # (row change, column change)

    def place_word(word):
        nonlocal letter_count
        placed = False
        attempts = 0

        while not placed and attempts < 100:
            direction = random.choice(directions)
            row_start = random.randint(0, grid_size - 1)
            col_start = random.randint(0, grid_size - 1)

            if direction == (0, 1):  # Horizontal
                if col_start + len(word) <= grid_size and all(grid[row_start][col_start + i] == '#' for i in range(len(word))):
                    for i, letter in enumerate(word):
                        if letter not in letter_to_number:
                            letter_to_number[letter] = letter_count
                            letter_count += 1
                        grid[row_start][col_start + i] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row_start][col_start + i] = letter
                    placed = True

            elif direction == (1, 0):  # Vertical
                if row_start + len(word) <= grid_size and all(grid[row_start + i][col_start] == '#' for i in range(len(word))):
                    for i, letter in enumerate(word):
                        if letter not in letter_to_number:
                            letter_to_number[letter] = letter_count
                            letter_count += 1
                        grid[row_start + i][col_start] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row_start + i][col_start] = letter
                    placed = True

            attempts += 1

    # Place only the requested number of words
    for word in selected_words:
        place_word(word.upper())

    return grid, solution_grid, letter_to_number


