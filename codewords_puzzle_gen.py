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

    # Ensure that only the requested number of words is placed
    word_list = word_list[:grid_size]  # Strictly limit to grid size or word count

    def place_word(word):
        nonlocal letter_count
        placed = False
        attempts = 0

        while not placed and attempts < 100:
            direction = random.choice(["H", "V"])
            if direction == "H":  # Place horizontally
                row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - len(word))
                if all(grid[row][col + i] == '#' for i in range(len(word))):  # Ensure space is empty
                    for i, letter in enumerate(word):
                        if letter not in letter_to_number:
                            letter_to_number[letter] = letter_count
                            letter_count += 1
                        grid[row][col + i] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row][col + i] = letter
                    placed = True
            else:  # Place vertically
                row, col = random.randint(0, grid_size - len(word)), random.randint(0, grid_size - 1)
                if all(grid[row + i][col] == '#' for i in range(len(word))):  # Ensure space is empty
                    for i, letter in enumerate(word):
                        if letter not in letter_to_number:
                            letter_to_number[letter] = letter_count
                            letter_count += 1
                        grid[row + i][col] = f"{letter}<sup>{letter_to_number[letter]}</sup>"
                        solution_grid[row + i][col] = letter
                    placed = True
            attempts += 1

    # Place the exact number of requested words
    for word in word_list:
        place_word(word.upper())

    return grid, solution_grid, letter_to_number

