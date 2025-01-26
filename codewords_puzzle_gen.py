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

# Generate codewords puzzle with the correct number of words
def generate_codewords_puzzle(word_list, grid_size):
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    solution_grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]
    letter_to_number = {}
    letter_count = 1

    # Limit words to the requested number
    if len(word_list) > grid_size:
        word_list = random.sample(word_list, grid_size)  # Randomly pick words if too many

    def place_word(word):
        nonlocal letter_count
        max_row, max_col = grid_size - len(word), grid_size

        # Ensure the placement stays within the grid
        if max_row < 0:
            return

        row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)

        for i, letter in enumerate(word):
            if letter not in letter_to_number:
                letter_to_number[letter] = letter_count
                letter_count += 1
            grid[row][col + i] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
            solution_grid[row][col + i] = letter

    # Place only the requested number of words
    for word in word_list[:grid_size]:
        place_word(word)

    return grid, solution_grid, letter_to_number

